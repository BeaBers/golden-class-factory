#!/usr/bin/env python3
# full_miner.py v4 - Golden Class Factory Full Mining (Improved)

import os, re, json, sys
from datetime import datetime
from pathlib import Path

ROOT = Path('C:/Users/Administrator/Desktop/WebProject')
RADIX = ROOT / "01-mines/web-mine/radix-ui/packages/react"
KV = ROOT / "01-mines/design-mine/konva/src"
WO = ROOT / "03-gold-boxes/web-props"
DO = ROOT / "03-gold-boxes/design-props"
RP_DIR = ROOT / "06-reports/mining-reports"
CP = ROOT / "mining_checkpoint.json"
LOG_DIR = ROOT / "logs"

WEB = ["accordion", "alert-dialog", "avatar", "checkbox", "collapsible", "dialog", "hover-card", "popover", "progress", "radio-group", "select", "slider", "switch", "tabs", "toast", "toggle", "toggle-group", "tooltip"]
DESIGN = ["Arc", "Arrow", "Circle", "Ellipse", "Image", "Label", "Line", "Path", "Rect", "RegularPolygon", "Ring", "Star", "Text", "TextPath", "Wedge"]

CSS = {"x": "left", "y": "top", "width": "width", "height": "height", "fill": "background-color", "stroke": "border-color", "strokeWidth": "border-width", "opacity": "opacity", "visible": "visibility", "rotation": "rotate", "cornerRadius": "border-radius", "shadowColor": "box-shadow-color", "shadowBlur": "box-shadow-blur-radius", "shadowOffset": "box-shadow-offset", "shadowOpacity": "box-shadow-opacity", "lineCap": "stroke-linecap", "lineJoin": "stroke-linejoin", "dash": "stroke-dasharray", "dashOffset": "stroke-dashoffset", "scaleX": "scaleX", "scaleY": "scaleY", "skewX": "skewX", "skewY": "skewY"}
TAGS = {"accordion": "div", "alert-dialog": "div", "avatar": "span", "checkbox": "button", "collapsible": "div", "dialog": "div", "hover-card": "div", "popover": "div", "progress": "div", "radio-group": "div", "select": "div", "slider": "span", "switch": "button", "tabs": "div", "toast": "li", "toggle": "button", "toggle-group": "div", "tooltip": "div"}


def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_DIR/"mining.log", "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [{level}] {msg}\n")
    if level in ("ERROR","WARN"):
        with open(LOG_DIR/"errors.log", "a", encoding="utf-8") as f:
            f.write(f"[{ts}] [{level}] {msg}\n")
    print(f"  [{level}] {msg}")

def load_cp():
    if CP.exists():
        d = json.loads(open(CP,"r",encoding="utf-8-sig").read())
        if "processed" not in d and "processed_files" in d: d["processed"] = d["processed_files"]
        if "extracted" not in d and "extracted_elements" in d: d["extracted"] = d["extracted_elements"]
        if "processed" not in d: d["processed"] = []
        if "extracted" not in d: d["extracted"] = []
        return d
    return {"processed":[],"extracted":[]}

def save_cp(cp):
    with open(CP,"w",encoding="utf-8") as f:
        json.dump(cp,f,indent=2,ensure_ascii=False)

def read_file(p):
    try:
        if not p.exists(): return None
        return open(p,"r",encoding="utf-8-sig").read()
    except: return None

def map_type(t):
    t=t.strip()
    if t=="boolean": return "boolean","toggle",None
    if t=="string": return "string","text_input",None
    if t=="number": return "number","slider",None
    if "'" in t and "|" in t:
        vals=[v.strip().strip("'") for v in t.split("|") if v.strip()]
        return "enum","select",vals
    if "Function" in t or t.startswith("(") or "=>" in t or "):" in t:
        return "function","code_input",None
    if "[]" in t or t.startswith("Array") or t.startswith("Array<"): return "array","text_input",None
    if "React.ReactNode" in t or "ReactNode" in t: return "component","component_picker",None
    if "React.Element" in t: return "component","component_picker",None
    if "MouseEvent" in t or "KeyboardEvent" in t: return "function","code_input",None
    return "string","text_input",None

def cat(n):
    n=n.lower()
    if n in ("x","y","width","height","offset","offsetx","offsety","min","max"): return "dimension"
    if any(v in n for v in ["fill","stroke","shadow","opacity","visible","dash","line","corner","blur","filter","gradient"]): return "visual"
    if any(v in n for v in ["drag","listening","hit","pointer","prevent","click"]): return "interaction"
    if any(v in n for v in ["scale","rotation","skew","transform"]): return "transform"
    if any(v in n for v in ["disabled","checked","pressed","enabled","selected","readonly"]): return "state"
    if any(v in n for v in ["value","default","children","label","name","id","key"]): return "content"
    return "behavior"


def extract_jsdoc(lines, idx):
    """Extract JSDoc comments above a property line"""
    desc = ""; default_val = None
    i = idx - 1
    while i >= 0:
        line = lines[i].strip()
        if line.startswith("*/"): break
        if line.startswith("*"):
            text = line.lstrip("*").strip()
            if text.startswith("@defaultValue"):
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
        else: break
        i -= 1
    return desc.strip(), default_val


def extract_block(content, si):
    """Extract balanced braces block"""
    depth = 0; i = si
    while i < len(content):
        c = content[i]
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0: return i
        i += 1
    return len(content)

def parse_ts(body_lines, source_name=""):
    """Parse TypeScript interface body lines into props with JSDoc"""
    props = []
    lines = body_lines.split("\n") if isinstance(body_lines, str) else body_lines
    if isinstance(lines, str): lines = [lines]
    for idx, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith(("//","/*","*","}","[","]")): continue
        # Strip parenthesized function params
        cln = re.sub(r"\([^)]*\)","",line)
        m = re.match(r"(?P<n>\w+)\s*(?P<o>\??)\s*:\s*(?P<t>[^;]+?)\s*;?\s*$", cln)
        if not m: continue
        n = m.group("n"); ot = m.group("o"); rt = m.group("t").strip()
        if n in ("string","number","boolean","any","unknown","readonly","key","typeof"): continue
        # JSDoc
        desc, default_val = extract_jsdoc(lines, idx) if isinstance(lines, list) else ("", None)
        js, ui, av = map_type(rt)
        prop = {
            "name": n,
            "type": js,
            "required": ot != "?",
            "default": default_val,
            "allowedValues": av,
            "description": desc,
            "uiControl": ui,
            "category": cat(n),
            "constraints": None,
        }
        if js == "number" and not prop["constraints"]: prop["constraints"] = {"min": 0}
        props.append(prop)
    return props

# Improved regex patterns that handle extends and generics
INTERFACE_PATTERN = r"(?:interface|type)\s+(\w+Props?\w*)(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\{"

def extract_all(content):
    """Extract all props from all interfaces in source content"""
    allp = []
    for m in re.finditer(INTERFACE_PATTERN, content):
        si = m.end() - 1
        ei = extract_block(content, si)
        body = content[si+1:ei]
        # If body has nested braces, try to handle them via the block extraction (already done)
        lines = body.split("\n")
        for p in parse_ts(lines, m.group(1)):
            if p["name"] not in [x["name"] for x in allp]:
                allp.append(p)
    return allp

def extract_type(content, tname):
    """Extract props from a specific named type"""
    for pat in [
        r"interface\s+" + re.escape(tname) + r"(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\{",
        r"type\s+" + re.escape(tname) + r"(?:<[^>]*>)?\s*=\s*(?:[^{]*?\&\s*)?\{",
    ]:
        m = re.search(pat, content)
        if m:
            si = m.end() - 1
            ei = extract_block(content, si)
            lines = content[si+1:ei].split("\n")
            return parse_ts(lines, tname)
    return []


def get_events(cname):
    ev = []
    cl = cname.lower()
    if any(x in cl for x in ["dialog","popover","tooltip","hover-card","menu"]):
        ev.append({"name":"onOpenChange","desc":"Open state changes","params":["boolean"]})
    if any(x in cl for x in ["select","radio","toggle","switch","checkbox"]):
        ev.append({"name":"onValueChange","desc":"Value changes","params":["string|boolean"]})
    if "accordion" in cl:
        ev.append({"name":"onValueChange","desc":"Expanded item changes","params":["string[]"]})
    if "slider" in cl:
        ev.append({"name":"onValueChange","desc":"Slider value changes","params":["number[]"]})
    if "tabs" in cl:
        ev.append({"name":"onValueChange","desc":"Active tab changes","params":["string"]})
    if "progress" in cl:
        ev.append({"name":"onValueChange","desc":"Progress value changes","params":["number"]})
    if "toggle" in cl or "switch" in cl:
        ev.append({"name":"onPressedChange","desc":"Pressed state changes","params":["boolean"]})
    ev.extend([
        {"name":"onClick","desc":"Clicked","params":["React.MouseEvent"]},
        {"name":"onFocus","desc":"Focused","params":["React.FocusEvent"]},
        {"name":"onBlur","desc":"Blurred","params":["React.FocusEvent"]},
    ])
    return ev

def get_access(cl):
    aria = ["aria-label","aria-describedby"]
    kb = {}
    if any(x in cl for x in ["dialog","popover","menu","tooltip"]):
        aria += ["aria-modal","aria-hidden"]
        kb = {"Escape":"Close","Tab":"Cycle focus"}
    if any(x in cl for x in ["button","toggle","switch","checkbox","radio"]):
        aria += ["aria-pressed","aria-checked","aria-disabled"]
        kb = {"Space":"Toggle","Enter":"Activate"}
    if "select" in cl:
        aria += ["aria-expanded","aria-controls","aria-activedescendant"]
        kb = {"ArrowDown":"Open/Next","ArrowUp":"Previous","Enter":"Select","Escape":"Close"}
    if "tabs" in cl:
        aria += ["aria-selected","aria-tablist","aria-controls"]
        kb = {"ArrowRight":"Next","ArrowLeft":"Previous","Home":"First","End":"Last"}
    if "slider" in cl:
        aria += ["aria-valuemin","aria-valuemax","aria-valuenow","aria-orientation"]
        kb = {"ArrowRight":"Increase","ArrowLeft":"Decrease"}
    if "accordion" in cl:
        aria += ["aria-expanded","aria-controls"]
        kb = {"Space":"Toggle","Enter":"Toggle"}
    return {"aria": aria, "kb": kb}


def mine_radix():
    cp = load_cp(); ext = []
    if not RADIX.exists():
        log("Radix path not found: " + str(RADIX), "ERROR")
        return ext
    log("Starting Radix UI mining...")
    for comp in WEB:
        if comp in cp.get("extracted", []):
            log(comp + " already processed", "INFO")
            ext.append(comp); continue
        src = RADIX / comp / "src"
        if not src.exists():
            log(comp + ": no src folder", "WARN")
            continue
        content = None; fp = None
        for e in [".tsx", ".ts"]:
            c = src / f"{comp}{e}"
            if c.exists(): content = read_file(c); fp = c; break
        if not content:
            i = src / "index.ts"
            if i.exists(): content = read_file(i); fp = i
        if not content:
            for f in sorted(src.glob("*.tsx")):
                content = read_file(f); fp = f; break
        if not content:
            log(comp + ": no source file found", "WARN")
            continue
        props = extract_all(content)
        # Also try specific type name variants
        for tn in [comp.title() + "Props", comp.title().replace("-","") + "Props"]:
            nprops = extract_type(content, tn)
            for p in nprops:
                if p["name"] not in [x["name"] for x in props]: props.append(p)
        # Try compound component patterns
        parts = comp.split("-")
        if len(parts) > 1:
            for i2 in range(1, len(parts)+1):
                tn = "".join(p.title() for p in parts[:i2]) + "Props"
                if tn != comp.title() + "Props":
                    nprops = extract_type(content, tn)
                    for p in nprops:
                        if p["name"] not in [x["name"] for x in props]: props.append(p)
        ev = get_events(comp)
        acc = get_access(comp.lower())
        tag = TAGS.get(comp, "div")
        data = {
            "meta": {"name": comp.title(), "source": "Radix UI", "ver": "1.0.0", "date": datetime.now().strftime("%Y-%m-%d"), "type": "web"},
            "sem": {"tag": tag, "container": False, "children": True, "role": comp.lower()},
            "props": props, "events": ev, "access": acc
        }
        WO.mkdir(parents=True, exist_ok=True)
        with open(WO / f"{comp.title()}_v2.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log(f"{comp}: {len(props)}p {len(ev)}e", "OK")
        ext.append(comp)
        cp.setdefault("processed", []).append(str(fp))
        cp.setdefault("extracted", []).append(comp)
        save_cp(cp)
    return ext


def mine_konva():
    cp = load_cp(); ext = []
    log("Starting Konva.js mining...")
    nc = read_file(KV / "Node.ts")
    sc = read_file(KV / "Shape.ts")
    cc = read_file(KV / "Container.ts")
    bn = extract_type(nc, "NodeConfig") if nc else []
    bs = extract_type(sc, "ShapeConfig") if sc else []
    bc = extract_type(cc, "ContainerConfig") if cc else []
    allb = bn + bs + bc; seen = set(); bp = []
    for p in allb:
        if p["name"] not in seen: seen.add(p["name"]); bp.append(p)
    for p in bp:
        if p["name"] == "visible": p["default"] = True
        elif p["name"] == "listening": p["default"] = True
        elif p["name"] == "draggable": p["default"] = False
        elif p["name"] == "opacity": p["default"] = 1
        elif p["name"] == "rotation": p["default"] = 0
        p["css"] = CSS.get(p["name"], None)
        p["cat"] = cat(p["name"])
        if p["type"] == "number" and not p.get("constraints"): p["constraints"] = {"min": 0}
    for sn in DESIGN:
        if sn in cp.get("extracted", []):
            log(sn + " already processed", "INFO")
            ext.append(sn); continue
        f = KV / f"shapes/{sn}.ts"
        if not f.exists():
            log(sn + ": file not found", "WARN")
            continue
        content = read_file(f)
        if not content: continue
        props = [p.copy() for p in bp]
        sp = extract_type(content, sn + "Config")
        for p in sp:
            if p["name"] not in [x["name"] for x in props]:
                p["css"] = CSS.get(p["name"], None)
                p["constraints"] = {"min": 0} if p["type"] == "number" else None
                p["cat"] = cat(p["name"])
                if p["name"] == "cornerRadius": p["default"] = 0
                props.append(p)
        ev = [
            {"name":"click","params":["MouseEvent"]},{"name":"dblclick","params":["MouseEvent"]},
            {"name":"mousedown","params":["MouseEvent"]},{"name":"mouseup","params":["MouseEvent"]},
            {"name":"mouseenter","params":["MouseEvent"]},{"name":"mouseleave","params":["MouseEvent"]},
            {"name":"touchstart","params":["TouchEvent"]},{"name":"touchend","params":["TouchEvent"]},
            {"name":"dragstart","params":["DragEvent"]},{"name":"dragmove","params":["DragEvent"]},
            {"name":"dragend","params":["DragEvent"]},{"name":"transform","params":["Event"]},
        ]
        caps = {"freeform": sn=="Path", "path": sn in ("Path","Line"), "corners": sn in ("Rect","Image","RegularPolygon"), "blend": True, "grad": True}
        data = {
            "meta": {"name": sn, "source": "Konva.js", "ver": "10.3.0", "date": datetime.now().strftime("%Y-%m-%d"), "type": "design"},
            "props": props, "events": ev, "caps": caps
        }
        DO.mkdir(parents=True, exist_ok=True)
        with open(DO / f"{sn}_v2.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log(f"{sn}: {len(props)}p {len(ev)}e", "OK")
        ext.append(sn)
        cp.setdefault("processed", []).append(str(f))
        cp.setdefault("extracted", []).append(sn)
        save_cp(cp)
    return ext


MIN_JSON_SIZE = 5000
MIN_PROPS_COUNT = 3

def validate_json_quality(json_file):
    """Validate quality of extracted JSON file"""
    issues = []
    # 1. File size check
    file_size = os.path.getsize(json_file)
    if file_size < 1000:
        issues.append(f"CRITICAL: file too small ({file_size} bytes)")
    elif file_size < MIN_JSON_SIZE:
        issues.append(f"WARNING: file size low ({file_size} bytes, expected >{MIN_JSON_SIZE})")
    try:
        with open(json_file, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except:
        issues.append("CRITICAL: invalid JSON")
        return issues
    # 2. Props count
    props_count = len(data.get("props", []))
    if props_count == 0:
        issues.append("CRITICAL: no props extracted")
    elif props_count < MIN_PROPS_COUNT:
        issues.append(f"WARNING: only {props_count} props")
    # 3. Description check
    empty_desc = sum(1 for p in data.get("props", []) if not p.get("description","").strip())
    total_props = len(data.get("props", []))
    if total_props > 0 and empty_desc > total_props * 0.5:
        issues.append(f"WARNING: {empty_desc}/{total_props} props have no description")
    elif empty_desc > 0 and total_props > 0:
        issues.append(f"INFO: {empty_desc}/{total_props} props without description")
    # 4. uiControl check
    no_ui = sum(1 for p in data.get("props", []) if not p.get("uiControl"))
    if no_ui > 0:
        issues.append(f"INFO: {no_ui} props without uiControl")
    # 5. Events check
    ev_count = len(data.get("events", []))
    if ev_count == 0:
        issues.append("INFO: no events extracted")
    # 6. default values check
    defaults = sum(1 for p in data.get("props", []) if p.get("default") is not None)
    return issues


def generate_automatic_report(web, design):
    """Generate comprehensive quality report"""
    lines = []
    def L(s=""): lines.append(s)
    L("=" * 60)
    L("FULL MINING - QUALITY REPORT")
    L("=" * 60)
    L(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    L("")

    web_files = sorted(WO.glob("*.json"))
    design_files = sorted(DO.glob("*.json"))
    L(f"Web mine: {len(web_files)} files")
    L(f"Design mine: {len(design_files)} files")
    L("")

    L("QUALITY VALIDATION RESULTS:")
    L("-" * 60)
    L("")

    all_issues = {}
    total_critical = 0
    total_warnings = 0

    for jf in web_files + design_files:
        issues = validate_json_quality(jf)
        if issues:
            all_issues[jf.name] = issues
            for iss in issues:
                if iss.startswith("CRITICAL"): total_critical += 1
                elif iss.startswith("WARNING"): total_warnings += 1

    if not all_issues:
        L("  All files passed quality check!")
    else:
        for fname, issues in sorted(all_issues.items()):
            L(f"  {fname}:")
            for iss in issues:
                L(f"    {iss}")
            L("")

    total_files = len(web_files) + len(design_files)
    files_with_issues = len(all_issues)
    clean_files = total_files - files_with_issues

    L("=" * 60)
    L("SUMMARY:")
    L(f"  Total files: {total_files}")
    L(f"  Clean files: {clean_files}")
    L(f"  Files with issues: {files_with_issues}")
    L(f"  Critical issues: {total_critical}")
    L(f"  Warnings: {total_warnings}")
    if total_files > 0:
        quality = round((clean_files / total_files) * 100, 1)
        L(f"  Quality score: {quality}%")
    L("=" * 60)

    # Save report
    RP_DIR.mkdir(parents=True, exist_ok=True)
    rp = RP_DIR / "automatic_quality_report.txt"
    open(rp, "w", encoding="utf-8").write("\n".join(lines))
    log(f"Quality report saved: {rp}")

    # Print to console
    for line in lines:
        print(line)

    return total_critical, total_warnings, clean_files, total_files


if __name__ == "__main__":
    import time
    start = time.time()
    print("=" * 60)
    print("  GOLDEN CLASS FACTORY - FULL MINER v4")
    print("=" * 60)
    print()
    try:
        print("[1/4] Mining Radix UI (web)...")
        web = mine_radix()
        print()
        print("[2/4] Mining Konva.js (design)...")
        design = mine_konva()
        print()
        print("[3/4] Validating quality...")
        crit, warns, clean, total = generate_automatic_report(web, design)
        print()
        print("[4/4] Summary...")
        elapsed = round(time.time() - start, 1)
        print(f"  Time: {elapsed}s")
        print(f"  Web: {len(web)}/{len(WEB)} components")
        print(f"  Design: {len(design)}/{len(DESIGN)} shapes")
        print(f"  Quality: {clean}/{total} clean files")
        print(f"  Critical issues: {crit}")
        print(f"  Warnings: {warns}")
    except Exception as e:
        log(f"FATAL: {str(e)}", "ERROR")
        import traceback
        traceback.print_exc()
    print()
    print("=" * 60)
    print("  DONE")
    print("=" * 60)
