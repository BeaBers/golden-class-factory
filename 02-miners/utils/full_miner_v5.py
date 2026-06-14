#!/usr/bin/env python3
# full_miner_v5.py - Golden Class Factory Ultimate Mining Engine
# جودة فائقة: استخراج دقيق مع أوصاف ذكية، CSS كامل، هيكل متكامل

import os, re, json, sys
from datetime import datetime
from pathlib import Path

ROOT = Path('C:/Users/Administrator/Desktop/WebProject')
RADIX = ROOT / '01-mines/web-mine/radix-ui/packages/react'
KV = ROOT / '01-mines/design-mine/konva/src'
WO = ROOT / '03-gold-boxes/web-props'
DO = ROOT / '03-gold-boxes/design-props'
RP_DIR = ROOT / '06-reports/mining-reports'
CP = ROOT / 'mining_checkpoint.json'
LOG_DIR = ROOT / 'logs'

WEB = ['accordion','alert-dialog','avatar','checkbox','collapsible','dialog','hover-card','popover','progress','radio-group','select','slider','switch','tabs','toast','toggle','toggle-group','tooltip']
DESIGN = ['Arc','Arrow','Circle','Ellipse','Image','Label','Line','Path','Rect','RegularPolygon','Ring','Star','Text','TextPath','Wedge']

# ============================================================
# CSS MAP COMPLETE - كل ما يقابل CSS
# ============================================================
CSS_MAP = {
    "x": "left", "y": "top", "width": "width", "height": "height",
    "minWidth": "min-width", "minHeight": "min-height",
    "maxWidth": "max-width", "maxHeight": "max-height",
    "offset": "transform-origin", "offsetX": "transform-origin (X)", "offsetY": "transform-origin (Y)",
    "fill": "background-color", "fillEnabled": None, "fillPriority": "background",
    "fillRule": "clip-rule", "fillPatternImage": "background-image",
    "fillPatternX": "background-position-x", "fillPatternY": "background-position-y",
    "fillPatternOffset": "background-position", "fillPatternOffsetX": "background-position (X)",
    "fillPatternOffsetY": "background-position (Y)", "fillPatternScale": "background-size",
    "fillPatternScaleX": "background-size (X)", "fillPatternScaleY": "background-size (Y)",
    "fillPatternRotation": "background (rotation)", "fillPatternRepeat": "background-repeat",
    "fillLinearGradientStartPoint": "background: linear-gradient (start)",
    "fillLinearGradientStartPointX": "background: linear-gradient (start X)",
    "fillLinearGradientStartPointY": "background: linear-gradient (start Y)",
    "fillLinearGradientEndPoint": "background: linear-gradient (end)",
    "fillLinearGradientEndPointX": "background: linear-gradient (end X)",
    "fillLinearGradientEndPointY": "background: linear-gradient (end Y)",
    "fillLinearGradientColorStops": "background: linear-gradient (stops)",
    "fillRadialGradientStartPoint": "background: radial-gradient (start)",
    "fillRadialGradientStartPointX": "background: radial-gradient (start X)",
    "fillRadialGradientStartPointY": "background: radial-gradient (start Y)",
    "fillRadialGradientEndPoint": "background: radial-gradient (end)",
    "fillRadialGradientEndPointX": "background: radial-gradient (end X)",
    "fillRadialGradientEndPointY": "background: radial-gradient (end Y)",
    "fillRadialGradientStartRadius": "background: radial-gradient (start radius)",
    "fillRadialGradientEndRadius": "background: radial-gradient (end radius)",
    "fillRadialGradientColorStops": "background: radial-gradient (stops)",
    "fillAfterStrokeEnabled": None,
    "stroke": "border-color", "strokeWidth": "border-width",
    "strokeScaleEnabled": None, "strokeHitEnabled": None, "strokeEnabled": None,
    "hitStrokeWidth": None, "lineJoin": "stroke-linejoin", "lineCap": "stroke-linecap",
    "miterLimit": "stroke-miterlimit",
    "cornerRadius": "border-radius",
    "borderWidth": "border-width", "borderColor": "border-color", "borderStyle": "border-style",
    "shadowColor": "box-shadow-color", "shadowBlur": "box-shadow-blur-radius",
    "shadowOffset": "box-shadow-offset", "shadowOffsetX": "box-shadow (offset X)",
    "shadowOffsetY": "box-shadow (offset Y)", "shadowOpacity": "box-shadow-opacity",
    "shadowEnabled": None, "shadowForStrokeEnabled": None,
    "dash": "stroke-dasharray", "dashOffset": "stroke-dashoffset", "dashEnabled": None,
    "opacity": "opacity", "visible": "visibility",
    "globalCompositeOperation": "mix-blend-mode",
    "filters": "filter (CSS functions)", "blendMode": "mix-blend-mode",
    "rotation": "transform: rotate(Ndeg)", "rotationDeg": "transform: rotate(Ndeg)",
    "scale": "transform: scale(N)", "scaleX": "transform: scaleX(N)",
    "scaleY": "transform: scaleY(N)", "skewX": "transform: skewX(Ndeg)",
    "skewY": "transform: skewY(Ndeg)",
    "fontSize": "font-size", "fontFamily": "font-family", "fontStyle": "font-style",
    "fontWeight": "font-weight", "fontVariant": "font-variant",
    "lineHeight": "line-height", "letterSpacing": "letter-spacing",
    "textAlign": "text-align", "verticalAlign": "vertical-align",
    "textDecoration": "text-decoration", "textTransform": "text-transform",
    "color": "color", "textColor": "color",
    "direction": "direction", "wordSpacing": "word-spacing",
    "textShadow": "text-shadow", "whiteSpace": "white-space",
    "overflow": "overflow", "textOverflow": "text-overflow",
    "gap": "gap", "padding": "padding",
    "paddingTop": "padding-top", "paddingRight": "padding-right",
    "paddingBottom": "padding-bottom", "paddingLeft": "padding-left",
    "margin": "margin", "marginTop": "margin-top", "marginRight": "margin-right",
    "marginBottom": "margin-bottom", "marginLeft": "margin-left",
    "flexDirection": "flex-direction", "flexWrap": "flex-wrap",
    "justifyContent": "justify-content", "alignItems": "align-items",
    "alignContent": "align-content", "alignSelf": "align-self",
    "flex": "flex", "flexGrow": "flex-grow", "flexShrink": "flex-shrink",
    "flexBasis": "flex-basis", "order": "order",
    "gridTemplate": "grid-template", "gridColumn": "grid-column",
    "gridRow": "grid-row", "gridArea": "grid-area",
    "position": "position", "top": "top", "right": "right", "bottom": "bottom", "left": "left",
    "zIndex": "z-index",
    "background": "background", "backgroundColor": "background-color",
    "backgroundImage": "background-image", "backgroundSize": "background-size",
    "backgroundPosition": "background-position", "backgroundRepeat": "background-repeat",
    "border": "border", "borderRadius": "border-radius",
    "borderTop": "border-top", "borderRight": "border-right",
    "borderBottom": "border-bottom", "borderLeft": "border-left",
    "outline": "outline", "outlineWidth": "outline-width",
    "outlineStyle": "outline-style", "outlineColor": "outline-color",
    "outlineOffset": "outline-offset",
    "cursor": "cursor", "pointerEvents": "pointer-events",
    "userSelect": "user-select", "resize": "resize",
    "transition": "transition", "transform": "transform",
    "animation": "animation", "animationName": "animation-name",
    "animationDuration": "animation-duration",
    "animationTimingFunction": "animation-timing-function",
    "animationDelay": "animation-delay",
    "animationIterationCount": "animation-iteration-count",
    "animationDirection": "animation-direction",
    "animationFillMode": "animation-fill-mode",
    "boxShadow": "box-shadow",
    "listStyle": "list-style", "listStyleType": "list-style-type",
    "id": "id (HTML attribute)", "className": "class", "name": "name (HTML attribute)",
    "value": "value (HTML attribute)", "placeholder": "placeholder",
    "title": "title (HTML attribute)", "alt": "alt (HTML attribute)",
    "src": "src (HTML attribute)", "href": "href (HTML attribute)",
    "target": "target (HTML attribute)", "rel": "rel (HTML attribute)",
    "type": "type (HTML attribute)", "disabled": "disabled (HTML attribute)",
    "readOnly": "readonly (HTML attribute)", "required": "required (HTML attribute)",
    "autoFocus": "autofocus (HTML attribute)", "tabIndex": "tabindex",
    "draggable": None, "dragDistance": None, "dragBoundFunc": None,
    "preventDefault": None, "listening": None,
    "hitFunc": None, "sceneFunc": None, "clipFunc": None,
    "clipX": "clip-path (X)", "clipY": "clip-path (Y)",
    "clipWidth": "clip-path (width)", "clipHeight": "clip-path (height)",
    "clearBeforeDraw": None, "perfectDrawEnabled": None,
    "asChild": None, "as": None,
    "defaultOpen": None, "open": None,
    "defaultValue": None, "defaultChecked": None, "checked": None,
    "onCheckedChange": None, "onOpenChange": None,
    "onValueChange": None, "onClick": None, "onFocus": None, "onBlur": None,
    "forceMount": None,
}

# ============================================================
# SMART DESCRIPTION GENERATOR - أوصاف ذكية بالعربية
# ============================================================
DESC_TEMPLATES = {
    "x": "الإحداثي الأفقي (X) للعنصر من الزاوية اليسرى",
    "y": "الإحداثي الرأسي (Y) للعنصر من الزاوية العلوية",
    "width": "عرض العنصر بالبكسل",
    "height": "ارتفاع العنصر بالبكسل",
    "fill": "لون تعبئة الخلفية",
    "stroke": "لون الحدود الخارجية",
    "strokeWidth": "سماكة الحدود الخارجية بالبكسل",
    "opacity": "درجة الشفافية (0=شفاف تماماً، 1=معتم)",
    "visible": "التحكم في ظهور/إخفاء العنصر",
    "rotation": "زاوية الدوران بالدرجات",
    "rotationDeg": "زاوية الدوران بالدرجات",
    "cornerRadius": "نصف قطر تدوير الزوايا",
    "shadowColor": "لون الظل",
    "shadowBlur": "مقدار ضبابية الظل بالبكسل",
    "shadowOffsetX": "إزاحة الظل أفقياً بالبكسل",
    "shadowOffsetY": "إزاحة الظل رأسياً بالبكسل",
    "shadowOpacity": "شفافية الظل",
    "scaleX": "مقياس التكبير/التصغير الأفقي",
    "scaleY": "مقياس التكبير/التصغير الرأسي",
    "skewX": "إمالة أفقية بالدرجات",
    "skewY": "إمالة رأسية بالدرجات",
    "dash": "نمط الخط المتقطع (مصفوفة أرقام)",
    "dashOffset": "إزاحة بداية نمط الخط المتقطع",
    "lineCap": "شكل نهاية الخط (butt/round/square)",
    "lineJoin": "شكل التقاء الخطوط (miter/round/bevel)",
    "miterLimit": "الحد الأقصى لزاوية miter",
    "draggable": "السماح بسحب العنصر بالماوس",
    "disabled": "تعطيل التفاعل مع العنصر",
    "fontSize": "حجم الخط بالبكسل",
    "fontFamily": "نوع الخط المستخدم",
    "fontWeight": "سماكة الخط (400=عادي، 700=عريض)",
    "textAlign": "محاذاة النص أفقياً",
    "verticalAlign": "محاذاة النص رأسياً",
    "lineHeight": "ارتفاع السطر",
    "letterSpacing": "المسافة بين الأحرف",
    "color": "لون النص",
    "textColor": "لون النص",
    "padding": "الحشوة الداخلية بالبكسل",
    "margin": "الهامش الخارجي بالبكسل",
    "gap": "المسافة بين العناصر الفرعية",
    "flexDirection": "اتجاه ترتيب العناصر (row/column)",
    "flexWrap": "السماح بالتفاف العناصر لسطر جديد",
    "justifyContent": "محاذاة العناصر على المحور الرئيسي",
    "alignItems": "محاذاة العناصر على المحور العرضي",
    "borderWidth": "سماكة الحدود بالبكسل",
    "borderColor": "لون الحدود",
    "borderRadius": "نصف قطر تدوير الزوايا",
    "variant": "نمط المظهر (solid/outline/ghost/link)",
    "size": "حجم المكون (sm/md/lg)",
    "label": "النص المعروض على المكون",
    "placeholder": "نص تلميحي يظهر عند الفراغ",
    "id": "معرف فريد للعنصر (HTML id)",
    "className": "فئة CSS إضافية للعنصر",
    "name": "اسم العنصر (يُستخدم للنماذج)",
    "value": "القيمة الحالية للعنصر",
    "defaultValue": "القيمة الافتراضية للعنصر",
    "checked": "حالة التحديد (true/false)",
    "defaultChecked": "حالة التحديد الافتراضية",
    "required": "حقل إجباري",
    "readOnly": "للقراءة فقط",
    "autoFocus": "التركيز التلقائي عند التحميل",
    "tabIndex": "ترتيب التنقل باستخدام Tab",
    "asChild": "استخدام عنصر HTML مخصص بدلاً من الافتراضي",
    "as": "تحديد عنصر HTML بديل",
    "forceMount": "فرض بقاء المكون في DOM حتى عند إخفائه",
    "defaultOpen": "الحالة الافتراضية للفتح/الإغلاق",
    "open": "التحكم في فتح/إغلاق المكون",
    "listening": "الاستماع للأحداث (true/false)",
    "hitStrokeWidth": "عرض منطقة الاصطدام للحدود",
    "strokeScaleEnabled": "تمكين تكبير/تصغير الحدود",
    "strokeEnabled": "تفعيل رسم الحدود",
    "fillEnabled": "تفعيل تعبئة الشكل",
    "fillPriority": "أولوية التعبئة (color/gradient/pattern)",
    "fillRule": "قاعدة التعبئة (nonzero/evenodd)",
    "globalCompositeOperation": "طريقة مزج الألوان مع الخلفية",
    "filters": "مرشحات Canvas (blur, brightness, etc.)",
    "sceneFunc": "دالة رسم مخصصة للمشهد",
    "hitFunc": "دالة رسم مخصصة لمنطقة الاصطدام",
    "clipFunc": "دالة قص مخصصة",
    "clipX": "إحداثي X لمساحة القص",
    "clipY": "إحداثي Y لمساحة القص",
    "clipWidth": "عرض مساحة القص",
    "clipHeight": "ارتفاع مساحة القص",
    "clearBeforeDraw": "مسح القماش قبل الرسم",
    "perfectDrawEnabled": "تفعيل الرسم المثالي",
    "shadowEnabled": "تفعيل الظل",
    "shadowForStrokeEnabled": "تفعيل الظل للحدود",
    "dashEnabled": "تفعيل نمط الخط المتقطع",
    "dragDistance": "المسافة الدنيا قبل بدء السحب",
    "dragBoundFunc": "دالة تحديد حدود السحب",
    "preventDefault": "منع السلوك الافتراضي",
    "offset": "نقطة الارتكاز (transform-origin)",
    "offsetX": "نقطة الارتكاز الأفقية",
    "offsetY": "نقطة الارتكاز الرأسية",
    "scale": "مقياس التكبير/التصغير الكلي",
    "fillPatternImage": "صورة نمط التعبئة",
    "fillPatternX": "إزاحة نمط التعبئة أفقياً",
    "fillPatternY": "إزاحة نمط التعبئة رأسياً",
    "fillPatternOffset": "إزاحة نمط التعبئة",
    "fillPatternOffsetX": "إزاحة نمط التعبئة أفقياً",
    "fillPatternOffsetY": "إزاحة نمط التعبئة رأسياً",
    "fillPatternScale": "مقياس نمط التعبئة",
    "fillPatternScaleX": "مقياس نمط التعبئة أفقي",
    "fillPatternScaleY": "مقياس نمط التعبئة رأسي",
    "fillPatternRotation": "دوران نمط التعبئة",
    "fillPatternRepeat": "تكرار نمط التعبئة",
    "fillLinearGradientStartPoint": "نقطة بداية التدرج الخطي",
    "fillLinearGradientStartPointX": "X نقطة بداية التدرج الخطي",
    "fillLinearGradientStartPointY": "Y نقطة بداية التدرج الخطي",
    "fillLinearGradientEndPoint": "نقطة نهاية التدرج الخطي",
    "fillLinearGradientEndPointX": "X نقطة نهاية التدرج الخطي",
    "fillLinearGradientEndPointY": "Y نقطة نهاية التدرج الخطي",
    "fillLinearGradientColorStops": "نقاط توقف ألوان التدرج الخطي",
    "fillRadialGradientStartPoint": "نقطة بداية التدرج الشعاعي",
    "fillRadialGradientStartPointX": "X نقطة بداية التدرج الشعاعي",
    "fillRadialGradientStartPointY": "Y نقطة بداية التدرج الشعاعي",
    "fillRadialGradientEndPoint": "نقطة نهاية التدرج الشعاعي",
    "fillRadialGradientEndPointX": "X نقطة نهاية التدرج الشعاعي",
    "fillRadialGradientEndPointY": "Y نقطة نهاية التدرج الشعاعي",
    "fillRadialGradientStartRadius": "نصف قطر بداية التدرج الشعاعي",
    "fillRadialGradientEndRadius": "نصف قطر نهاية التدرج الشعاعي",
    "fillRadialGradientColorStops": "نقاط توقف ألوان التدرج الشعاعي",
    "fillAfterStrokeEnabled": "تعبئة الشكل بعد رسم الحدود",
    "strokeHitEnabled": "تمكين اصطدام الحدود",
    "perfectDrawEnabled": "تحسين جودة الرسم",
}

def css_for(name):
    """Get CSS equivalent for a property name"""
    return CSS_MAP.get(name, None)

def desc_for(name, ptype, default_val):
    """Generate smart description for any property"""
    if name in DESC_TEMPLATES:
        d = DESC_TEMPLATES[name]
        if ptype == "boolean" and default_val is not None:
            d += f" (الافتراضي: {default_val})"
        return d
    # Generate generic description
    ar_desc = {
        "accordion": "مكون أكورديون لعرض محتوى قابل للطي",
        "alert-dialog": "مربع حوار تنبيهي يتطلب إجراء",
        "avatar": "مكون صورة رمزية للمستخدم",
        "checkbox": "مربع اختيار",
        "collapsible": "مكون قابل للطي/التوسيع",
        "dialog": "مربع حوار منبثق",
        "hover-card": "بطاقة تظهر عند تمرير الماوس",
        "popover": "نافذة منبثقة",
        "progress": "شريط تقدم",
        "radio-group": "مجموعة خيارات دائرية (اختيار واحد)",
        "select": "قائمة منسدلة للاختيار",
        "slider": "شريط تمرير لاختيار قيمة",
        "switch": "مفتاح تشغيل/إيقاف",
        "tabs": "علامات تبويب",
        "toast": "إشعار مؤقت",
        "toggle": "زر تبديل (تشغيل/إيقاف)",
        "toggle-group": "مجموعة أزرار تبديل",
        "tooltip": "تلميح نصي يظهر عند التمرير",
    }
    base_desc = ar_desc.get(name.lower(), f"خاصية {name}")
    tdesc = {"boolean": " (منطقي)", "number": " (رقمي)", "string": " (نصي)",
             "function": " (دالة)", "array": " (مصفوفة)", "enum": " (قيم محددة)",
             "component": " (مكون React)"}
    return base_desc + tdesc.get(ptype, "")

def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_DIR/"mining_v5.log", "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [{level}] {msg}\n")
    if level in ("ERROR","WARN"):
        with open(LOG_DIR/"errors.log", "a", encoding="utf-8") as f:
            f.write(f"[{ts}] [{level}] {msg}\n")
    print(f"  [{level}] {msg}")

def load_cp():
    if CP.exists():
        d = json.loads(open(CP, "r", encoding="utf-8-sig").read())
        if "processed" not in d: d["processed"] = []
        if "extracted" not in d: d["extracted"] = []
        return d
    return {"processed": [], "extracted": []}

def save_cp(cp):
    with open(CP, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2, ensure_ascii=False)

def read_file(p):
    try:
        if not p.exists(): return None
        return open(p, "r", encoding="utf-8-sig").read()
    except: return None

def map_type(t):
    t = t.strip()
    if t == "boolean": return "boolean", "toggle", None
    if t == "string": return "string", "text_input", None
    if t == "number": return "number", "slider", None
    if "'" in t and "|" in t:
        vals = [v.strip().strip("'") for v in t.split("|") if v.strip()]
        return "enum", "select", vals
    if "Function" in t or t.startswith("(") or "=>" in t or "):" in t:
        return "function", "code_input", None
    if "[]" in t or t.startswith("Array"):
        return "array", "text_input", None
    if any(x in t for x in ["React.ReactNode", "ReactNode", "React.Element"]):
        return "component", "component_picker", None
    if any(x in t for x in ["MouseEvent", "KeyboardEvent", "FocusEvent", "TouchEvent"]):
        return "function", "code_input", None
    return "string", "text_input", None

def categorize(name):
    n = name.lower()
    if n in ("x","y","width","height","minwidth","minheight","maxwidth","maxheight","offset","offsetx","offsety"):
        return "dimension"
    if n in ("size","fontsize","fontfamily","fontweight","fontstyle","fontvariant","lineheight","letterspacing","wordspacing","textalign","verticalalign","textdecoration","texttransform","textshadow","whitespace","textoverflow","direction"):
        return "typography"
    if n in ("gap","padding","margin","paddingtop","paddingright","paddingbottom","paddingleft","margintop","marginright","marginbottom","marginleft","flexdirection","flexwrap","justifycontent","alignitems","aligncontent","alignself","flex","flexgrow","flexshrink","flexbasis","order","gridtemplate","gridcolumn","gridrow","gridarea","position","top","right","bottom","left","zindex"):
        return "layout"
    if any(v in n for v in ["fill","stroke","shadow","opacity","visible","dash","linejoin","linecap","miter","corner","blur","filter","border","outline","gradient","pattern","blend","background","color"]):
        return "visual"
    if n in ("rotation","rotationdeg","scale","scalex","scaley","skewx","skewy","transform"):
        return "transform"
    if any(v in n for v in ["drag","listening","hit","prevent","click","scroll"]):
        return "interaction"
    if n in ("disabled","checked","pressed","enabled","selected","readonly","required"):
        return "state"
    if n in ("value","defaultvalue","defaultchecked","defaultopen","open","label","placeholder","id","classname","name","title","alt","src","href","target","rel","type","tabindex","autofocus"):
        return "content"
    if any(v in n for v in ["aschild","as","forcemount","children"]):
        return "behavior"
    if any(v in n for v in ["aria","role"]):
        return "accessibility"
    return "behavior"

INTERFACE_PATTERN = r"(?:interface|type)\s+(\w+)(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\{"

def extract_block(content, si):
    depth = 0; i = si
    while i < len(content):
        c = content[i]
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0: return i
        i += 1
    return len(content)

def extract_jsdoc_v2(lines, idx):
    """Improved JSDoc - handles blank lines between comment and property"""
    desc = ""; default_val = None
    i = idx - 1
    while i >= 0:
        line = lines[i].strip()
        if line == "":
            i -= 1; continue
        if line.startswith("*/"):
            i -= 1; continue
        if line.startswith("*"):
            text = line.lstrip("*").strip()
            if text.startswith("@param"): pass
            elif text.startswith("@defaultValue"):
                dv = text[len("@defaultValue"):].strip()
                if dv: default_val = dv
            elif text.startswith("@default"):
                dv = text[len("@default"):].strip()
                if dv: default_val = dv
            elif text and not text.startswith("@"):
                if desc: desc = text + " " + desc
                else: desc = text
        elif line.startswith("/**"):
            text = line.lstrip("/**").strip().lstrip("*").strip()
            if text:
                if text.startswith("@defaultValue"):
                    dv = text[len("@defaultValue"):].strip()
                    if dv: default_val = dv
                elif text.startswith("@default"):
                    dv = text[len("@default"):].strip()
                    if dv: default_val = dv
                elif not text.startswith("@"):
                    if desc: desc = text + " " + desc
                    else: desc = text
            break
        elif line.startswith(("}",")","]")):
            break
        elif re.match(r"^\w+\s*\??\s*:", line):
            break
        else: break
        i -= 1
    return desc.strip(), default_val

def parse_ts_v2(body_lines, source_name=""):
    """Parse TypeScript with smart descriptions"""
    props = []
    lines = body_lines.split("\n") if isinstance(body_lines, str) else body_lines
    if isinstance(lines, str): lines = [lines]
    for idx, line in enumerate(lines):
        raw = line; line = line.strip()
        if not line or line.startswith(("//","/*","*","}","[","]")): continue
        cln = re.sub(r"\([^)]*\)", "", line)
        m = re.match(r"(?P<n>\w+)\s*(?P<o>\??)\s*:\s*(?P<t>[^;]+?)\s*;?\s*$", cln)
        if not m: continue
        n = m.group("n"); ot = m.group("o"); rt = m.group("t").strip()
        if n in ("string","number","boolean","any","unknown","readonly","key","typeof"): continue
        desc, default_val = extract_jsdoc_v2(lines, idx)
        js, ui, av = map_type(rt)
        if not desc:
            desc = desc_for(n, js, default_val)
        prop = {
            "name": n, "type": js, "required": ot != "?",
            "default": default_val, "allowedValues": av,
            "description": desc, "uiControl": ui,
            "category": categorize(n), "constraints": None,
            "css": css_for(n),
        }
        if js == "number" and not prop.get("constraints"):
            prop["constraints"] = {"min": 0}
        props.append(prop)
    return props

def extract_all_v2(content):
    allp = []
    for m in re.finditer(INTERFACE_PATTERN, content):
        si = m.end() - 1
        ei = extract_block(content, si)
        body = content[si+1:ei]
        for p in parse_ts_v2(body.split("\n"), m.group(1)):
            if p["name"] not in [x["name"] for x in allp]:
                allp.append(p)
    return allp

def extract_type_v2(content, tname):
    for pat in [
        r"interface\s+" + re.escape(tname) + r"(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\{",
        r"type\s+" + re.escape(tname) + r"(?:<[^>]*>)?\s*=\s*(?:[^{]*?\&\s*)?\{",
    ]:
        m = re.search(pat, content)
        if m:
            si = m.end() - 1
            ei = extract_block(content, si)
            return parse_ts_v2(content[si+1:ei].split("\n"), tname)
    return []

# ============================================================
# COMPONENT HIERARCHY - هيكل المكونات المركبة
# ============================================================
COMPOUND_PARTS = {
    "accordion": ["Root", "Item", "Header", "Trigger", "Content"],
    "alert-dialog": ["Root", "Trigger", "Portal", "Overlay", "Content", "Title", "Description", "Cancel", "Action"],
    "avatar": ["Root", "Image", "Fallback"],
    "checkbox": ["Root", "Indicator"],
    "collapsible": ["Root", "Trigger", "Content"],
    "dialog": ["Root", "Trigger", "Portal", "Overlay", "Content", "Title", "Description", "Close"],
    "hover-card": ["Root", "Trigger", "Portal", "Content"],
    "popover": ["Root", "Trigger", "Portal", "Content", "Close", "Arrow"],
    "progress": ["Root", "Indicator"],
    "radio-group": ["Root", "Item", "Indicator"],
    "select": ["Root", "Trigger", "Content", "Item", "ItemText", "ItemIndicator", "ScrollUpButton", "ScrollDownButton", "Value", "Icon", "Portal", "Group", "Label", "Separator"],
    "slider": ["Root", "Track", "Range", "Thumb"],
    "switch": ["Root", "Thumb"],
    "tabs": ["Root", "List", "Trigger", "Content"],
    "toast": ["Root", "Provider", "Viewport", "Title", "Description", "Close", "Action"],
    "toggle": ["Root"],
    "toggle-group": ["Root", "Item"],
    "tooltip": ["Root", "Trigger", "Portal", "Content", "Arrow"],
}

RADIX_EVENTS_BASE = [
    {"name": "onClick", "params": ["React.MouseEvent"], "description": "عند النقر على المكون"},
    {"name": "onFocus", "params": ["React.FocusEvent"], "description": "عند اكتساب التركيز"},
    {"name": "onBlur", "params": ["React.FocusEvent"], "description": "عند فقدان التركيز"},
]

def get_component_events(cname):
    cl = cname.lower()
    ev = list(RADIX_EVENTS_BASE)
    open_close = ["dialog","popover","tooltip","hover-card","alert-dialog","collapsible"]
    value_change = ["select","radio-group","toggle","switch","checkbox","slider","progress","tabs","accordion","toggle-group"]
    if cl in open_close:
        ev.insert(0, {"name":"onOpenChange","params":["boolean"],"description":"عند تغيير حالة الفتح/الإغلاق"})
    if cl in value_change:
        desc_map = {"accordion":"عند تغيير العنصر الموسع","slider":"عند تغيير قيمة التمرير","tabs":"عند تغيير التبويب النشط","progress":"عند تغيير قيمة التقدم","toggle":"عند تغيير حالة الضغط","switch":"عند تغيير حالة التشغيل","checkbox":"عند تغيير حالة الاختيار","radio-group":"عند تغيير الخيار المحدد","select":"عند تغيير القيمة المحددة","toggle-group":"عند تغيير العنصر المحدد"}
        param_map = {"accordion":"string[]","slider":"number[]","tabs":"string","progress":"number"}
        pm = param_map.get(cl, "string|boolean")
        ev.insert(0, {"name":"onValueChange","params":[pm],"description":desc_map.get(cl,"عند تغيير القيمة")})
    add_events = {
        "dialog": [{"name":"onEscapeKeyDown","params":["KeyboardEvent"],"description":"عند الضغط على Escape"}],
        "select": [{"name":"onCloseAutoFocus","params":["Event"],"description":"عند إغلاق القائمة مع التركيز التلقائي"}],
        "toast": [{"name":"onSwipe","params":["Event"],"description":"عند التمرير السريع"}],
    }
    if cl in add_events:
        ev.extend(add_events[cl])
    return ev

KONVA_EVENTS = [
    {"name":"click","params":["MouseEvent"],"description":"عند النقر على الشكل"},
    {"name":"dblclick","params":["MouseEvent"],"description":"عند النقر المزدوج"},
    {"name":"mousedown","params":["MouseEvent"],"description":"عند الضغط على زر الفأرة"},
    {"name":"mouseup","params":["MouseEvent"],"description":"عند رفع زر الفأرة"},
    {"name":"mouseenter","params":["MouseEvent"],"description":"عند دخول مؤشر الفأرة"},
    {"name":"mouseleave","params":["MouseEvent"],"description":"عند خروج مؤشر الفأرة"},
    {"name":"touchstart","params":["TouchEvent"],"description":"عند لمس الشاشة"},
    {"name":"touchend","params":["TouchEvent"],"description":"عند رفع اللمس"},
    {"name":"dragstart","params":["DragEvent"],"description":"عند بدء السحب"},
    {"name":"dragmove","params":["DragEvent"],"description":"أثناء السحب"},
    {"name":"dragend","params":["DragEvent"],"description":"عند انتهاء السحب"},
    {"name":"transform","params":["Event"],"description":"عند التحويل (تكبير/تدوير)"},
    {"name":"mousewheel","params":["WheelEvent"],"description":"عند تدوير عجلة الفأرة"},
    {"name":"contextmenu","params":["MouseEvent"],"description":"عند النقر بزر الفأرة الأيمن"},
]

# ============================================================
# MINE RADIX UI v5
# ============================================================
def mine_radix_v5():
    cp = load_cp(); ext = []
    if not RADIX.exists():
        log("مسار Radix UI غير موجود", "ERROR"); return ext
    log("=== بدء تعدين Radix UI v5 ===")
    for comp in WEB:
        if comp in cp.get("extracted",[]):
            log(f"{comp}: سبق معالجته"); continue
        src = RADIX / comp / "src"
        if not src.exists():
            log(f"{comp}: لا يوجد src", "WARN"); continue
        content = None; fp = None
        for e in [".tsx",".ts"]:
            c = src / f"{comp}{e}"
            if c.exists(): content = read_file(c); fp = c; break
        if not content:
            i = src / "index.ts"
            if i.exists(): content = read_file(i); fp = i
        if not content:
            for f in sorted(src.glob("*.tsx")):
                content = read_file(f); fp = f; break
        if not content:
            log(f"{comp}: لا يوجد ملف مصدر", "WARN"); continue
        props = extract_all_v2(content)
        comp_title = comp.title().replace("-","")
        for tn in [comp.title()+"Props", comp_title+"Props"]:
            for p in extract_type_v2(content, tn):
                if p["name"] not in [x["name"] for x in props]: props.append(p)
        parts = comp.split("-")
        if len(parts) > 1:
            for i2 in range(1, len(parts)+1):
                tn = "".join(p.title() for p in parts[:i2]) + "Props"
                if tn != comp.title()+"Props" and tn != comp_title+"Props":
                    for p in extract_type_v2(content, tn):
                        if p["name"] not in [x["name"] for x in props]: props.append(p)
        cat_order = {"dimension":0,"layout":1,"visual":2,"typography":3,"transform":4,"interaction":5,"state":6,"content":7,"behavior":8,"accessibility":9}
        props.sort(key=lambda p: (cat_order.get(p["category"],99), p["name"]))
        ev = get_component_events(comp)
        parts_list = COMPOUND_PARTS.get(comp, [comp.title()])
        tag = "div"
        if comp in ["checkbox","switch","toggle"]: tag = "button"
        elif comp in ["avatar"]: tag = "span"
        elif comp in ["toast"]: tag = "li"
        hierarchy = {}
        for part in parts_list:
            hierarchy[part] = {"tag": tag, "children": True}
        data = {
            "meta": {"name": comp.title(), "source": "Radix UI Primitives",
                     "ver": "1.0.0", "date": datetime.now().strftime("%Y-%m-%d"),
                     "type": "web", "miner": "full_miner_v5"},
            "hierarchy": {"root": parts_list[0] if parts_list else comp.title(),
                          "parts": parts_list, "structure": hierarchy},
            "props": props, "events": ev,
        }
        WO.mkdir(parents=True, exist_ok=True)
        with open(WO / f"{comp.title()}_v5.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log(f"{comp}: {len(props)} خاصية، {len(ev)} حدث ✅")
        ext.append(comp)
        cp.setdefault("processed",[]).append(str(fp))
        cp.setdefault("extracted",[]).append(comp)
        save_cp(cp)
    return ext

# ============================================================
# MINE KONVA.JS v5
# ============================================================
def mine_konva_v5():
    cp = load_cp(); ext = []
    log("=== بدء تعدين Konva.js v5 ===")
    nc = read_file(KV / "Node.ts") or ""
    sc = read_file(KV / "Shape.ts") or ""
    cc = read_file(KV / "Container.ts") or ""
    bn = extract_type_v2(nc, "NodeConfig") if nc else []
    bs = extract_type_v2(sc, "ShapeConfig") if sc else []
    bc = extract_type_v2(cc, "ContainerConfig") if cc else []
    allb = bn + bs + bc; seen = set(); bp = []
    for p in allb:
        if p["name"] not in seen: seen.add(p["name"]); bp.append(p)
    for p in bp:
        if p["name"] == "visible": p["default"] = True
        elif p["name"] == "listening": p["default"] = True
        elif p["name"] == "draggable": p["default"] = False
        elif p["name"] == "opacity": p["default"] = 1
        elif p["name"] == "rotation": p["default"] = 0
        elif p["name"] == "cornerRadius": p["default"] = 0
        p["description"] = desc_for(p["name"], p["type"], p["default"])
        p["css"] = css_for(p["name"])
        p["category"] = p.get("category") or categorize(p["name"])
        if p["type"] == "number" and not p.get("constraints"):
            p["constraints"] = {"min": 0}
    bp.sort(key=lambda p: ({"dimension":0,"visual":1,"transform":2,"interaction":3,"content":4,"behavior":5}.get(categorize(p["name"]),99), p["name"]))
    for sn in DESIGN:
        if sn in cp.get("extracted",[]):
            log(f"{sn}: سبق معالجته"); ext.append(sn); continue
        f = KV / f"shapes/{sn}.ts"
        if not f.exists(): log(f"{sn}: ملف غير موجود", "WARN"); continue
        content = read_file(f)
        if not content: continue
        props = [p.copy() for p in bp]
        for p in extract_type_v2(content, sn+"Config"):
            if p["name"] not in [x["name"] for x in props]:
                p["description"] = desc_for(p["name"], p["type"], p["default"])
                p["css"] = css_for(p["name"])
                p["constraints"] = {"min": 0} if p["type"] == "number" else None
                p["category"] = categorize(p["name"])
                if p["name"] == "cornerRadius": p["default"] = 0
                props.append(p)
        props.sort(key=lambda p: ({"dimension":0,"visual":1,"transform":2,"interaction":3,"content":4,"behavior":5}.get(categorize(p["name"]),99), p["name"]))
        caps = {"freeform": sn=="Path", "path": sn in ("Path","Line"),
                "corners": sn in ("Rect","Image","RegularPolygon"), "blend": True, "grad": True}
        data = {
            "meta": {"name": sn, "source": "Konva.js", "ver": "10.3.0",
                     "date": datetime.now().strftime("%Y-%m-%d"), "type": "design",
                     "miner": "full_miner_v5"},
            "props": props, "events": KONVA_EVENTS, "caps": caps,
        }
        DO.mkdir(parents=True, exist_ok=True)
        with open(DO / f"{sn}_v5.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log(f"{sn}: {len(props)} خاصية، {len(KONVA_EVENTS)} حدث ✅")
        ext.append(sn)
        cp.setdefault("processed",[]).append(str(f))
        cp.setdefault("extracted",[]).append(sn)
        save_cp(cp)
    return ext

# ============================================================
# QUALITY VALIDATION v5
# ============================================================
def validate_v5(json_file):
    issues = []
    file_size = os.path.getsize(json_file)
    try:
        with open(json_file, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except:
        issues.append("CRITICAL: ملف JSON تالف"); return issues
    props = data.get("props", []); pcount = len(props)
    if pcount == 0:
        name = data.get("meta",{}).get("name","?")
        issues.append(f"INFO: {name} ليس له خاصيات (موروث من مكون آخر)")
    empty_desc = sum(1 for p in props if not p.get("description","").strip())
    if pcount > 0 and empty_desc > 0:
        issues.append(f"INFO: {empty_desc}/{pcount} بدون وصف مخصص")
    no_css = sum(1 for p in props if not p.get("css") and p["type"] not in ("function",))
    if no_css > pcount * 0.3 and pcount > 5:
        issues.append(f"INFO: {no_css}/{pcount} بلا CSS (خصائص Canvas)")
    no_cat = sum(1 for p in props if not p.get("category"))
    if no_cat > 0:
        issues.append(f"INFO: {no_cat}/{pcount} بلا تصنيف")
    defaults = sum(1 for p in props if p.get("default") is not None)
    issues.append(f"PASS: {pcount} خاصية، {defaults} قيمة افتراضية، {len(data.get('events',[]))} حدث")
    return issues

def generate_report_v5(web_list, design_list):
    lines = []
    def L(s=""): lines.append(s)
    L("=" * 70)
    L("GOLDEN CLASS FACTORY - v5 QUALITY REPORT")
    L("=" * 70)
    L(f"التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    L("")
    web_files = sorted(WO.glob("*_v5.json"))
    design_files = sorted(DO.glob("*_v5.json"))
    L(f"صناديق الويب: {len(web_files)}")
    L(f"صناديق التصميم: {len(design_files)}")
    L("")
    L("نتائج التحقق من الجودة:")
    L("-" * 70)
    L("")
    all_issues = {}
    for jf in web_files + design_files:
        issues = validate_v5(jf)
        if issues: all_issues[jf.name] = issues
    for fname, issues in sorted(all_issues.items()):
        L(f"  {fname}:")
        for iss in issues:
            if iss.startswith("CRITICAL"): L(f"    CRITICAL: {iss}")
            elif iss.startswith("WARNING"): L(f"    WARNING: {iss}")
            elif iss.startswith("INFO"): L(f"    INFO: {iss}")
            elif iss.startswith("PASS"): L(f"    PASS: {iss}")
        L("")
    total = len(web_files)+len(design_files)
    clean = sum(1 for v in all_issues.values() if not any(i.startswith("CRITICAL") for i in v))
    L("=" * 70)
    L("SUMMARY:")
    L(f"  Total boxes: {total}")
    L(f"  No critical issues: {clean}")
    L(f"  Checked: {len(all_issues)}")
    qual = round((clean/total)*100,1) if total>0 else 0
    L(f"  Quality score: {qual}%")
    L("=" * 70)
    total_props = 0
    for jf in web_files+design_files:
        try:
            d = json.load(open(jf,"r",encoding="utf-8-sig"))
            total_props += len(d.get("props",[]))
        except: pass
    L(f"  Total extracted props: {total_props}")
    L("=" * 70)
    RP_DIR.mkdir(parents=True, exist_ok=True)
    rp = RP_DIR / "v5_quality_report.txt"
    open(rp, "w", encoding="utf-8").write("\n".join(lines))
    log(f"Quality report saved: {rp}")
    for line in lines: print(line)
    return total_props

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    import time
    start = time.time()
    print()
    print("=" * 70)
    print("  GOLDEN CLASS FACTORY - ULTIMATE MINER v5")
    print("  جودة فائقة - تعدين شامل - أوصاف ذكية")
    print("=" * 70)
    print()
    print("[1/4] Mining Radix UI (web)...")
    print()
    web = mine_radix_v5()
    print()
    print("[2/4] Mining Konva.js (design)...")
    print()
    design = mine_konva_v5()
    print()
    print("[3/4] Quality validation...")
    print()
    total_props = generate_report_v5(web, design)
    print()
    print("[4/4] Final summary...")
    elapsed = round(time.time()-start, 1)
    print(f"  Time: {elapsed}s")
    print(f"  Radix components: {len(web)}/{len(WEB)}")
    print(f"  Konva shapes: {len(design)}/{len(DESIGN)}")
    print(f"  Total props: {total_props}")
    print()
    print("=" * 70)
    print("  v5 mining complete!")
    print("=" * 70)
