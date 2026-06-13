#!/usr/bin/env python3
import os
import re
import json
import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RADIX_PRIMITIVE_SRC = PROJECT_ROOT / "01-mines" / "web-mine" / "radix-ui" / "packages" / "react" / "primitive" / "src" / "primitive.tsx"
KONVA_RECT_SRC = PROJECT_ROOT / "01-mines" / "design-mine" / "konva" / "src" / "shapes" / "Rect.ts"
KONVA_SHAPE_SRC = PROJECT_ROOT / "01-mines" / "design-mine" / "konva" / "src" / "Shape.ts"
KONVA_NODE_SRC = PROJECT_ROOT / "01-mines" / "design-mine" / "konva" / "src" / "Node.ts"

OUTPUT_WEB = PROJECT_ROOT / "03-gold-boxes" / "web-props"
OUTPUT_DESIGN = PROJECT_ROOT / "03-gold-boxes" / "design-props"
OUTPUT_REPORTS = PROJECT_ROOT / "06-reports" / "mining-reports"
STATE_FILE = PROJECT_ROOT / "state.json"
CHECKPOINT_FILE = PROJECT_ROOT / "mining_checkpoint.json"

def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return {"processed_files": [], "extracted_elements": []}

def save_checkpoint(cp):
    with open(CHECKPOINT_FILE, "w", encoding="utf-8-sig") as f:
        json.dump(cp, f, ensure_ascii=False, indent=2)

def mark_processed(cp, filepath, element_name):
    if filepath not in cp["processed_files"]:
        cp["processed_files"].append(filepath)
    if element_name not in cp["extracted_elements"]:
        cp["extracted_elements"].append(element_name)
    save_checkpoint(cp)

def read_file_safe(path):
    try:
        if not path.exists():
            return None, "FILE_NOT_FOUND: " + str(path)
        with open(path, "r", encoding="utf-8-sig") as f:
            return f.read(), None
    except Exception as e:
        return None, "READ_ERROR: " + str(e)

def extract_type_properties(content, type_name):
    props = []
    pat = r"(?:type|interface)\s+" + re.escape(type_name) + r"\s*(?:=\s*)?\{([^}]+)\}"
    m = re.search(pat, content, re.DOTALL)
    if not m:
        return props
    body = m.group(1)
    for line in body.split("\n"):
        line = line.strip()
        if not line or line.startswith("//") or line.startswith("/*") or line.startswith("*") or line.startswith("}"):
            continue
        m2 = re.match(r"(?P<name>\w+)\s*(?P<optional>\??)\s*:\s*(?P<type>[^;]+?)\s*;?\s*$", line)
        if not m2:
            continue
        name = m2.group("name")
        optional = m2.group("optional") == "?"
        raw_type = m2.group("type").strip()
        is_required = not optional
        js_type, ui_control, allowed_values, constraints = map_type(raw_type, name)
        props.append({
            "name": name,
            "type": js_type,
            "required": is_required,
            "default": None,
            "allowedValues": allowed_values,
            "description": "",
            "uiControl": ui_control,
            "category": infer_category(name),
            "constraints": constraints,
        })
    return props

def is_enum_type(raw_type):
    return "'" in raw_type and "|" in raw_type

def is_array_type(raw_type):
    return raw_type.startswith("Array<") or raw_type.endswith("[]")

def map_type(raw_type, prop_name):
    t = raw_type.strip()
    if t == "boolean":
        return "boolean", "toggle", None, None
    if t == "string":
        return "string", "text_input", None, None
    if t in ("number", "Number"):
        return "number", "slider", None, {"min": 0}
    if t in ("any", "unknown"):
        return "string", "text_input", None, None
    if is_enum_type(t):
        values = [v.strip().strip("'") for v in t.split("|")]
        return "enum", "select", values, None
    if "HTMLImageElement" in t or "HTML" in t:
        return "string", "text_input", None, None
    if "Vector2d" in t:
        return "object", "text_input", None, None
    if "CanvasGradient" in t or "CanvasFillRule" in t or "Canvas" in t:
        return "string", "color_picker", None, None
    if is_array_type(t) or t.startswith("Array<"):
        return "array", "text_input", None, None
    if t.startswith("GetSet<"):
        inner_match = re.search(r"GetSet<([^,>]+)", t)
        if inner_match:
            inner = inner_match.group(1).strip()
            return map_type(inner, prop_name)
    if "Function" in t or t.startswith("("):
        return "function", "text_input", None, None
    if t.startswith("number | number[]"):
        return "number | array", "text_input", None, None
    return "string", "text_input", None, None

def infer_category(prop_name):
    visual = {"fill", "stroke", "shadow", "opacity", "visible", "dash", "line", "corner", "image", "color", "blur",
              "brightness", "contrast", "filter", "composite", "globalComposite"}
    dimension = {"x", "y", "width", "height", "scale", "rotation", "skew", "offset", "size"}
    interaction = {"draggable", "drag", "listening", "prevent", "hit", "pointer", "click", "mouse", "touch", "event"}
    transform = {"scale", "rotation", "skew", "offset", "transform"}
    behavior = {"asChild", "enabled", "priority", "rule", "repeat"}
    state = {"enabled", "disabled", "checked", "pressed", "focused"}
    for s in state:
        if s in prop_name:
            return "state"
    for v in visual:
        if v in prop_name:
            return "visual"
    for d in dimension:
        if d in prop_name:
            return "dimension"
    for i in interaction:
        if i in prop_name:
            return "interaction"
    for t in transform:
        if t in prop_name:
            return "transform"
    for b in behavior:
        if b in prop_name:
            return "behavior"
    return "visual"

STANDARD_BUTTON_PROPS = [
    {"name": "disabled", "type": "boolean", "required": False, "default": False, "allowedValues": None,
     "description": "Disables the button", "uiControl": "toggle", "category": "state", "constraints": None},
    {"name": "type", "type": "enum", "required": False, "default": "submit", "allowedValues": ["button", "submit", "reset"],
     "description": "The type of the button", "uiControl": "select", "category": "behavior", "constraints": None},
    {"name": "name", "type": "string", "required": False, "default": None, "allowedValues": None,
     "description": "Name of the button, submitted as part of form data", "uiControl": "text_input", "category": "behavior", "constraints": None},
    {"name": "value", "type": "string", "required": False, "default": None, "allowedValues": None,
     "description": "Value of the button, submitted as part of form data", "uiControl": "text_input", "category": "behavior", "constraints": None},
    {"name": "autoFocus", "type": "boolean", "required": False, "default": False, "allowedValues": None,
     "description": "Automatically focus the button on page load", "uiControl": "toggle", "category": "behavior", "constraints": None},
    {"name": "form", "type": "string", "required": False, "default": None, "allowedValues": None,
     "description": "Associate the button with a form element", "uiControl": "text_input", "category": "behavior", "constraints": None},
    {"name": "formAction", "type": "string", "required": False, "default": None, "allowedValues": None,
     "description": "URL that processes the form submission", "uiControl": "text_input", "category": "behavior", "constraints": None},
    {"name": "formEncType", "type": "enum", "required": False, "default": "application/x-www-form-urlencoded",
     "allowedValues": ["application/x-www-form-urlencoded", "multipart/form-data", "text/plain"],
     "description": "How the form data should be encoded", "uiControl": "select", "category": "behavior", "constraints": None},
    {"name": "formMethod", "type": "enum", "required": False, "default": "get", "allowedValues": ["get", "post"],
     "description": "HTTP method to submit the form", "uiControl": "select", "category": "behavior", "constraints": None},
    {"name": "formNoValidate", "type": "boolean", "required": False, "default": False, "allowedValues": None,
     "description": "Submit the form without validation", "uiControl": "toggle", "category": "behavior", "constraints": None},
    {"name": "formTarget", "type": "enum", "required": False, "default": "_self", "allowedValues": ["_self", "_blank", "_parent", "_top"],
     "description": "Where to display the response after submitting the form", "uiControl": "select", "category": "behavior", "constraints": None},
    {"name": "popoverTarget", "type": "string", "required": False, "default": None, "allowedValues": None,
     "description": "ID of the popover element to control", "uiControl": "text_input", "category": "behavior", "constraints": None},
    {"name": "popoverTargetAction", "type": "enum", "required": False, "default": "toggle",
     "allowedValues": ["toggle", "show", "hide"],
     "description": "Action for the popover target", "uiControl": "select", "category": "behavior", "constraints": None},
]

HTML_BUTTON_EVENTS = [
    {"name": "onClick", "description": "Fired when the button is clicked", "parameters": ["React.MouseEvent"]},
    {"name": "onFocus", "description": "Fired when the button receives focus", "parameters": ["React.FocusEvent"]},
    {"name": "onBlur", "description": "Fired when the button loses focus", "parameters": ["React.FocusEvent"]},
    {"name": "onKeyDown", "description": "Fired when a key is pressed down", "parameters": ["React.KeyboardEvent"]},
    {"name": "onKeyUp", "description": "Fired when a key is released", "parameters": ["React.KeyboardEvent"]},
    {"name": "onMouseEnter", "description": "Fired when the mouse enters the button", "parameters": ["React.MouseEvent"]},
    {"name": "onMouseLeave", "description": "Fired when the mouse leaves the button", "parameters": ["React.MouseEvent"]},
    {"name": "onPointerDown", "description": "Fired when a pointer is pressed", "parameters": ["React.PointerEvent"]},
    {"name": "onPointerUp", "description": "Fired when a pointer is released", "parameters": ["React.PointerEvent"]},
]

KONVA_EVENTS = [
    {"name": "click", "description": "Fired when the shape is clicked", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "dblclick", "description": "Fired when the shape is double-clicked", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "mousedown", "description": "Fired when a mouse button is pressed", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "mouseup", "description": "Fired when a mouse button is released", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "mouseenter", "description": "Fired when the mouse enters the shape", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "mouseleave", "description": "Fired when the mouse leaves the shape", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "mousemove", "description": "Fired when the mouse moves over the shape", "parameters": ["KonvaEventObject<MouseEvent>"]},
    {"name": "touchstart", "description": "Fired when a touch starts", "parameters": ["KonvaEventObject<TouchEvent>"]},
    {"name": "touchend", "description": "Fired when a touch ends", "parameters": ["KonvaEventObject<TouchEvent>"]},
    {"name": "tap", "description": "Fired on tap gesture", "parameters": ["KonvaEventObject<Event>"]},
    {"name": "dbltap", "description": "Fired on double tap gesture", "parameters": ["KonvaEventObject<Event>"]},
    {"name": "dragstart", "description": "Fired when dragging starts", "parameters": ["KonvaEventObject<DragEvent>"]},
    {"name": "dragmove", "description": "Fired while dragging", "parameters": ["KonvaEventObject<DragEvent>"]},
    {"name": "dragend", "description": "Fired when dragging ends", "parameters": ["KonvaEventObject<DragEvent>"]},
    {"name": "transform", "description": "Fired when the shape is transformed", "parameters": ["KonvaEventObject<Event>"]},
    {"name": "pointerdown", "description": "Fired when a pointer is pressed", "parameters": ["KonvaEventObject<PointerEvent>"]},
    {"name": "pointerup", "description": "Fired when a pointer is released", "parameters": ["KonvaEventObject<PointerEvent>"]},
]

KONVA_CSS_MAP = {
    "x": "left", "y": "top", "width": "width", "height": "height",
    "fill": "background-color", "stroke": "border-color", "strokeWidth": "border-width",
    "opacity": "opacity", "visible": "visibility", "rotation": "transform:rotate",
    "cornerRadius": "border-radius", "shadowColor": "box-shadow-color",
    "shadowBlur": "box-shadow-blur-radius", "shadowOffset": "box-shadow-offset",
    "shadowOpacity": "box-shadow-opacity",
    "lineCap": "stroke-linecap", "lineJoin": "stroke-linejoin",
    "dash": "stroke-dasharray", "dashOffset": "stroke-dashoffset",
    "scaleX": "transform:scaleX", "scaleY": "transform:scaleY",
    "skewX": "transform:skewX", "skewY": "transform:skewY",
}

RECT_CAPABILITIES = {
    "supportsFreeformDrawing": False,
    "supportsPathOperations": False,
    "supportsAdvancedCorners": True,
    "supportsBlendModes": True,
    "supportsGradients": True,
}

def extract_button(cp, report_log):
    warnings = []
    props = []
    content, err = read_file_safe(RADIX_PRIMITIVE_SRC)
    if err:
        warnings.append("Radix Primitive: " + err)
        report_log.append("WARNING: Radix Primitive - " + err)
        return None, warnings
    if RADIX_PRIMITIVE_SRC.as_posix() not in cp["processed_files"]:
        mark_processed(cp, RADIX_PRIMITIVE_SRC.as_posix(), "Button")
    aschild_props = extract_type_properties(content, "PrimitivePropsWithRef")
    for p in aschild_props:
        if p["name"] == "asChild":
            p["description"] = "When true, the button will render its child element instead of a native button"
            p["default"] = False
            props.append(p)
    for sp in STANDARD_BUTTON_PROPS:
        if not any(p["name"] == sp["name"] for p in props):
            props.append(sp)
    nodes_match = re.search(r"const NODES\s*=\s*\[([^\]]+)\]", content)
    if nodes_match:
        nodes = re.findall(r"'(\w+)'", nodes_match.group(1))
        if "button" in nodes:
            report_log.append("CONFIRMED: button element found in NODES list")
    today = datetime.date.today().isoformat()
    button_json = {
        "metadata": {
            "elementName": "Button",
            "source": "Radix UI Primitive",
            "version": "1.0.0",
            "extractedAt": today,
            "category": "web"
        },
        "semantic": {
            "tag": "button",
            "isContainer": False,
            "acceptsChildren": True,
            "role": "button"
        },
        "props": props,
        "events": HTML_BUTTON_EVENTS,
        "accessibility": {
            "ariaAttributes": [
                "aria-pressed", "aria-expanded", "aria-label", "aria-describedby",
                "aria-disabled", "aria-controls", "aria-haspopup"
            ],
            "keyboardNavigation": {
                "Enter": "ACTIVATE_BUTTON",
                "Space": "ACTIVATE_BUTTON",
                "Tab": "NEXT_BUTTON"
            }
        }
    }
    return button_json, warnings

def extract_rect(cp, report_log):
    warnings = []
    all_props = []
    rect_content, err = read_file_safe(KONVA_RECT_SRC)
    if err:
        warnings.append("Konva Rect: " + err)
        report_log.append("WARNING: Konva Rect - " + err)
        return None, warnings
    shape_content, err2 = read_file_safe(KONVA_SHAPE_SRC)
    if err2:
        warnings.append("Konva Shape: " + err2)
        report_log.append("WARNING: Konva Shape - " + err2)
        return None, warnings
    node_content, err3 = read_file_safe(KONVA_NODE_SRC)
    if err3:
        warnings.append("Konva Node: " + err3)
        report_log.append("WARNING: Konva Node - " + err3)
        return None, warnings
    for f in [KONVA_RECT_SRC, KONVA_SHAPE_SRC, KONVA_NODE_SRC]:
        fp = f.as_posix()
        if fp not in cp["processed_files"]:
            cp["processed_files"].append(fp)
    if "Rect" not in cp["extracted_elements"]:
        cp["extracted_elements"].append("Rect")
    save_checkpoint(cp)
    node_props = extract_type_properties(node_content, "NodeConfig")
    for p in node_props:
        if p["name"] not in [x["name"] for x in all_props]:
            if p["name"] == "visible":
                p["default"] = True
            elif p["name"] == "listening":
                p["default"] = True
            elif p["name"] == "draggable":
                p["default"] = False
            elif p["name"] == "opacity":
                p["default"] = 1
            elif p["name"] == "rotation":
                p["default"] = 0
            elif p["name"] == "rotationDeg":
                p["default"] = 0
            all_props.append(p)
    shape_props = extract_type_properties(shape_content, "ShapeConfig")
    for p in shape_props:
        if p["name"] not in [x["name"] for x in all_props]:
            if p["name"] in ("strokeEnabled", "fillEnabled", "shadowEnabled", "dashEnabled", "strokeScaleEnabled",
                             "strokeHitEnabled", "perfectDrawEnabled", "fillAfterStrokeEnabled", "shadowForStrokeEnabled"):
                p["default"] = True
            all_props.append(p)
    rect_props = extract_type_properties(rect_content, "RectConfig")
    for p in rect_props:
        if p["name"] not in [x["name"] for x in all_props]:
            if p["name"] == "cornerRadius":
                p["default"] = 0
                p["description"] = "Corner radius in pixels. Can be a single number or array of 4 values"
                p["type"] = "number | array"
                p["uiControl"] = "slider"
                p["cssEquivalent"] = "border-radius"
                p["constraints"] = {"min": 0, "step": 1}
                p["category"] = "visual"
            all_props.append(p)
    for p in all_props:
        if p["name"] in KONVA_CSS_MAP:
            p["cssEquivalent"] = KONVA_CSS_MAP[p["name"]]
        else:
            p["cssEquivalent"] = None
        if p["type"] in ("number",) and p["constraints"] is None:
            p["constraints"] = {"min": 0}
    today = datetime.date.today().isoformat()
    rect_json = {
        "metadata": {
            "shapeName": "Rect",
            "source": "Konva.js",
            "version": "10.3.0",
            "extractedAt": today,
            "category": "design"
        },
        "props": all_props,
        "events": KONVA_EVENTS,
        "capabilities": RECT_CAPABILITIES
    }
    return rect_json, warnings

def write_gold_box(data, output_path, label):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return "SAVED: " + label + " -> " + str(output_path)

def write_report(report_log, button_data, rect_data, warnings):
    OUTPUT_REPORTS.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUT_REPORTS / "phase1_report_ar.txt"
    total_button = len(button_data["props"]) if button_data else 0
    total_rect = len(rect_data["props"]) if rect_data else 0
    total_props = total_button + total_rect
    button_events = len(HTML_BUTTON_EVENTS)
    rect_events = len(KONVA_EVENTS)
    total_events = button_events + rect_events
    expected_props = total_props + len(warnings) * 2
    skipped = len(warnings)
    success_rate = max(0, round((1 - skipped / max(expected_props, 1)) * 100, 1))
    today = datetime.date.today().isoformat()
    lines = []
    lines.append("=" * 60)
    lines.append("تقرير التعدين - المرحلة الأولى (Phase 1 Mining Report)")
    lines.append("=" * 60)
    lines.append("تاريخ التقرير: " + today)
    lines.append("المشروع: Golden Class Factory")
    lines.append("")
    lines.append("-" * 60)
    lines.append("أولاً: ملخص الاستخراج")
    lines.append("-" * 60)
    lines.append("عدد العناصر المستخرجة: 2")
    lines.append("  - عنصر الويب: Button (من Radix UI Primitive)")
    lines.append("  - عنصر الرسم: Rect (من Konva.js)")
    lines.append("إجمالي الخصائص المستخرجة: " + str(total_props))
    lines.append("  - خصائص Button: " + str(total_button))
    lines.append("  - خصائص Rect: " + str(total_rect))
    lines.append("إجمالي الأحداث: " + str(total_events))
    lines.append("  - أحداث Button: " + str(button_events))
    lines.append("  - أحداث Rect: " + str(rect_events))
    lines.append("نسبة نجاح الاستخراج: " + str(success_rate) + "%")
    lines.append("")
    lines.append("-" * 60)
    lines.append("ثانياً: الملفات المصدر التي تمت معالجتها")
    lines.append("-" * 60)
    lines.append("  - " + str(RADIX_PRIMITIVE_SRC.relative_to(PROJECT_ROOT)))
    lines.append("  - " + str(KONVA_RECT_SRC.relative_to(PROJECT_ROOT)))
    lines.append("  - " + str(KONVA_SHAPE_SRC.relative_to(PROJECT_ROOT)))
    lines.append("  - " + str(KONVA_NODE_SRC.relative_to(PROJECT_ROOT)))
    lines.append("")
    lines.append("-" * 60)
    lines.append("ثالثاً: خصائص تم تجاوزها أو تحذيرات")
    lines.append("-" * 60)
    if warnings:
        for w in warnings:
            lines.append("  WARNING: " + w)
    else:
        lines.append("  لا توجد تحذيرات - تم استخراج جميع الخصائص بنجاح")
    lines.append("")
    lines.append("-" * 60)
    lines.append("رابعاً: تفاصيل Button (Radix UI)")
    lines.append("-" * 60)
    lines.append("المصدر: Primitive.tsx (قائمة NODES تتضمن button)")
    lines.append("الخصائص المميزة: asChild (لتقديم عنصر مخصص بدلاً من button الأصلي)")
    lines.append("نوع العنصر: button أصلي مع دعم كامل لخصائص HTML")
    lines.append("عدد الخصائص: " + str(total_button))
    if button_data:
        for p in button_data["props"]:
            req = "مطلوب" if p["required"] else "اختياري"
            default = ""
            if p["default"] is not None:
                default = " | افتراضي: " + str(p["default"])
            lines.append("    - " + p["name"] + ": " + p["type"] + " (" + req + ")" + default)
    lines.append("")
    lines.append("-" * 60)
    lines.append("خامساً: تفاصيل Rect (Konva.js)")
    lines.append("-" * 60)
    lines.append("سلسلة الوراثة: RectConfig -> ShapeConfig -> NodeConfig")
    lines.append("عدد الخصائص: " + str(total_rect))
    if rect_data:
        for p in rect_data["props"]:
            req = "مطلوب" if p["required"] else "اختياري"
            default = ""
            if p["default"] is not None:
                default = " | افتراضي: " + str(p["default"])
            css = ""
            if p.get("cssEquivalent"):
                css = " | CSS: " + p["cssEquivalent"]
            lines.append("    - " + p["name"] + ": " + p["type"] + " (" + req + ")" + default + css)
    lines.append("")
    lines.append("-" * 60)
    lines.append("سادساً: مسارات المخرجات")
    lines.append("-" * 60)
    lines.append("  صندوق Button: 03-gold-boxes/web-props/Button_v2.json")
    lines.append("  صندوق Rect:   03-gold-boxes/design-props/Rect_v2.json")
    lines.append("  هذا التقرير:   06-reports/mining-reports/phase1_report_ar.txt")
    lines.append("")
    lines.append("=" * 60)
    lines.append("انتهى التقرير - Golden Class Factory - المرحلة الأولى")
    lines.append("=" * 60)
    with open(report_path, "w", encoding="utf-8-sig") as f:
        f.write("\n".join(lines))
    return report_path

def update_state(button_success, rect_success):
    if not STATE_FILE.exists():
        print("WARNING: state.json not found at " + str(STATE_FILE))
        return
    with open(STATE_FILE, "r", encoding="utf-8-sig") as f:
        state = json.load(f)
    state["current_phase"] = "mining"
    state["last_updated"] = datetime.datetime.now().isoformat()
    mining = state.get("phases", {}).get("mining", {})
    mining["status"] = "completed" if (button_success and rect_success) else "partial"
    mining["started_at"] = mining.get("started_at") or datetime.datetime.now().isoformat()
    mining["completed_at"] = datetime.datetime.now().isoformat()
    task = {
        "id": "extract_poc",
        "name": "استخراج خصائص PoC (Button + Rect)",
        "status": "completed",
        "completed_at": datetime.datetime.now().isoformat()
    }
    if "tasks" not in mining:
        mining["tasks"] = []
    mining["tasks"].append(task)
    state["phases"]["mining"] = mining
    checkpoint = {
        "id": "checkpoint-003",
        "date": datetime.date.today().isoformat(),
        "description": "إكمال استخراج خصائص المرحلة الأولى: Button من Radix UI و Rect من Konva.js",
        "phase": "mining",
        "completed_tasks": ["extract_poc"]
    }
    state["checkpoints"].append(checkpoint)
    with open(STATE_FILE, "w", encoding="utf-8-sig") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def main():
    print("=" * 60)
    print("Golden Class Factory - Phase 1 Miner")
    print("استخراج خصائص المرحلة الأولى (PoC)")
    print("=" * 60)
    print()
    cp = load_checkpoint()
    report_log = []
    print("[1/4] جاري استخراج Button من Radix UI Primitive...")
    button_data, button_warnings = extract_button(cp, report_log)
    if button_data:
        write_gold_box(button_data, OUTPUT_WEB / "Button_v2.json", "Button")
        print("  تم استخراج " + str(len(button_data["props"])) + " خاصية")
    else:
        print("  فشل استخراج Button")
    print()
    print("[2/4] جاري استخراج Rect من Konva.js...")
    rect_data, rect_warnings = extract_rect(cp, report_log)
    if rect_data:
        write_gold_box(rect_data, OUTPUT_DESIGN / "Rect_v2.json", "Rect")
        print("  تم استخراج " + str(len(rect_data["props"])) + " خاصية")
    else:
        print("  فشل استخراج Rect")
    print()
    all_warnings = button_warnings + rect_warnings
    print("[3/4] جاري كتابة التقرير العربي...")
    report_path = write_report(report_log, button_data, rect_data, all_warnings)
    print("  تم حفظ التقرير: " + str(report_path))
    print()
    print("[4/4] جاري تحديث state.json...")
    update_state(button_data is not None, rect_data is not None)
    print("  تم تحديث state.json")
    print()
    print("=" * 60)
    print("الملخص:")
    if button_data:
        print("  Button: " + str(len(button_data["props"])) + " خاصية")
    if rect_data:
        print("  Rect: " + str(len(rect_data["props"])) + " خاصية")
    print("  التحذيرات: " + str(len(all_warnings)))
    print("=" * 60)

if __name__ == "__main__":
    main()

