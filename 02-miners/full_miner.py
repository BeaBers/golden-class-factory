#!/usr/bin/env python3
# full_miner.py - Golden Class Factory Full Mining

import json, re, sys, os
from datetime import datetime
from pathlib import Path

ROOT = Path('C:/Users/Administrator/Desktop/WebProject')
RADIX = ROOT / "01-mines/web-mine/radix-ui/packages/react"
KV = ROOT / "01-mines/design-mine/konva/src"
WO = ROOT / "03-gold-boxes/web-props"
DO = ROOT / "03-gold-boxes/design-props"
RP = ROOT / "06-reports/mining-reports/full_mining_report_ar.txt"
CP = ROOT / "mining_checkpoint.json"

WEB = ["accordion", "alert-dialog", "avatar", "checkbox", "collapsible", "dialog", "hover-card", "popover", "progress", "radio-group", "select", "slider", "switch", "tabs", "toast", "toggle", "toggle-group", "tooltip"]
DESIGN = ["Arc", "Arrow", "Circle", "Ellipse", "Image", "Label", "Line", "Path", "Rect", "RegularPolygon", "Ring", "Star", "Text", "TextPath", "Wedge"]

CSS = {"x": "left", "y": "top", "width": "width", "height": "height", "fill": "background-color", "stroke": "border-color", "strokeWidth": "border-width", "opacity": "opacity", "visible": "visibility", "rotation": "rotate", "cornerRadius": "border-radius", "shadowColor": "box-shadow-color", "shadowBlur": "box-shadow-blur-radius", "shadowOffset": "box-shadow-offset", "shadowOpacity": "box-shadow-opacity", "lineCap": "stroke-linecap", "lineJoin": "stroke-linejoin", "dash": "stroke-dasharray", "dashOffset": "stroke-dashoffset", "scaleX": "scaleX", "scaleY": "scaleY", "skewX": "skewX", "skewY": "skewY"}
TAGS = {"accordion": "div", "alert-dialog": "div", "avatar": "span", "checkbox": "button", "collapsible": "div", "dialog": "div", "hover-card": "div", "popover": "div", "progress": "div", "radio-group": "div", "select": "div", "slider": "span", "switch": "button", "tabs": "div", "toast": "li", "toggle": "button", "toggle-group": "div", "tooltip": "div"}

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
    if "Function" in t or t.startswith("("): return "function","text_input",None
    if "[]" in t: return "array","text_input",None
    return "string","text_input",None

def cat(n):
    n=n.lower()
    if n in ("x","y","width","height","offset","offsetx","offsety"): return "dimension"
    if any(v in n for v in ["fill","stroke","shadow","opacity","visible","dash","line","corner","blur","filter"]): return "visual"
    if any(v in n for v in ["drag","listening","hit","pointer","prevent"]): return "interaction"
    if any(v in n for v in ["scale","rotation","skew","transform"]): return "transform"
    if any(v in n for v in ["disabled","checked","pressed","enabled"]): return "state"
    return "behavior"

def parse_ts(body):
    props=[]
    for line in body.split(chr(10)):
        line=line.strip()
        if not line or line.startswith(("//","/*","*","}","[","]")): continue
        cln = re.sub(chr(92)+chr(40)+chr(91)+chr(94)+chr(41)+chr(93)+chr(42)+chr(92)+chr(41),"",line)
        m=re.match(chr(40)+chr(63)+chr(80)+chr(60)+chr(110)+chr(62)+chr(92)+chr(119)+chr(43)+chr(41)+chr(92)+chr(115)+chr(42)+chr(40)+chr(63)+chr(80)+chr(60)+chr(111)+chr(62)+chr(92)+chr(63)+chr(63)+chr(41)+chr(92)+chr(115)+chr(42)+chr(58)+chr(92)+chr(115)+chr(42)+chr(40)+chr(63)+chr(80)+chr(60)+chr(116)+chr(62)+chr(91)+chr(94)+chr(59)+chr(93)+chr(43)+chr(63)+chr(41)+chr(92)+chr(115)+chr(42)+chr(59)+chr(63)+chr(92)+chr(115)+chr(42)+chr(36),cln)
        if m:
            print(f"    [DEBUG parse_ts] MATCH: {m.group(1)!r} -> {m.group(3)!r}", file=sys.stderr)
        else:
            print(f"    [DEBUG parse_ts] NO MATCH line: {line!r} cln: {cln!r}", file=sys.stderr)
            print(f"    [DEBUG parse_ts] Pattern: {chr(40)+chr(63)+chr(80)+chr(60)+chr(110)+chr(62)+chr(92)+chr(119)+chr(43)+chr(41)+chr(92)+chr(115)+chr(42)+chr(40)+chr(63)+chr(80)+chr(60)+chr(111)+chr(62)+chr(92)+chr(63)+chr(63)+chr(41)+chr(92)+chr(115)+chr(42)+chr(58)+chr(92)+chr(115)+chr(42)+chr(40)+chr(63)+chr(80)+chr(60)+chr(116)+chr(62)+chr(91)+chr(94)+chr(59)+chr(93)+chr(43)+chr(63)+chr(41)+chr(92)+chr(115)+chr(42)+chr(59)+chr(63)+chr(92)+chr(115)+chr(42)+chr(36)!r}", file=sys.stderr)
            continue
        n=m.group("n"); ot=m.group("o"); rt=m.group("t").strip()
        if n in ("string","number","boolean","any","unknown","readonly","key"): continue
        js,ui,av=map_type(rt)
        props.append({"name":n,"type":js,"required":ot!="?","default":None,"allowedValues":av,"description":"","uiControl":ui,"category":cat(n),"constraints":None})
    return props

def extract_block(content,si):
    depth=0; i=si
    while i<len(content):
        c=content[i]
        if c=='{': depth+=1
        elif c=='}':
            depth-=1
            if depth==0: return i
        i+=1
    return len(content)

def extract_type(content,tname):
    for pat in [
        "interface\\s+"+re.escape(tname)+"\\s*\\{",
        "type\\s+"+re.escape(tname)+"\\s*=\\s*\\{",
        "type\\s+"+re.escape(tname)+"\\s*=[^\\{]*?\\&\\s*\\{"
    ]:
        m=re.search(pat,content)
        if m:
            si=m.end()-1
            ei=extract_block(content,si)
            return parse_ts(content[si+1:ei])
    return []

def extract_all(content):
    allp=[]
    for m in re.finditer("(?:interface|type)\\s+(\\w+Props?\\w*)\\s*(?:=\\s*)?\\{",content):
        si=m.end()-1
        ei=extract_block(content,si)
        for p in parse_ts(content[si+1:ei]):
            if p["name"] not in [x["name"] for x in allp]: allp.append(p)
    return allp

def get_events(cname):
    ev=[]
    cl=cname.lower()
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
    ev.extend([{"name":"onClick","desc":"Clicked","params":["React.MouseEvent"]},{"name":"onFocus","desc":"Focused","params":["React.FocusEvent"]},{"name":"onBlur","desc":"Blurred","params":["React.FocusEvent"]}])
    return ev

def get_access(cl):
    aria=["aria-label","aria-describedby"]
    kb={}
    if any(x in cl for x in ["dialog","popover","menu","tooltip"]):
        aria+=["aria-modal","aria-hidden"]
        kb={"Escape":"Close","Tab":"Cycle focus"}
    if any(x in cl for x in ["button","toggle","switch","checkbox","radio"]):
        aria+=["aria-pressed","aria-checked","aria-disabled"]
        kb={"Space":"Toggle","Enter":"Activate"}
    if "select" in cl:
        aria+=["aria-expanded","aria-controls","aria-activedescendant"]
        kb={"ArrowDown":"Open/Next","ArrowUp":"Previous","Enter":"Select","Escape":"Close"}
    if "tabs" in cl:
        aria+=["aria-selected","aria-tablist","aria-controls"]
        kb={"ArrowRight":"Next","ArrowLeft":"Previous","Home":"First","End":"Last"}
    if "slider" in cl:
        aria+=["aria-valuemin","aria-valuemax","aria-valuenow","aria-orientation"]
        kb={"ArrowRight":"Increase","ArrowLeft":"Decrease"}
    if "accordion" in cl:
        aria+=["aria-expanded","aria-controls"]
        kb={"Space":"Toggle","Enter":"Toggle"}
    return {"aria":aria,"kb":kb}

def mine_radix():
    cp=load_cp(); ext=[]
    if not RADIX.exists(): print("  [FAIL] Radix path"); return ext
    for comp in WEB:
        if comp in cp.get("extracted",[]): print("  [SKIP] "+comp); ext.append(comp); continue
        src=RADIX/comp/"src"
        if not src.exists(): print("  [WARN] "+comp+": no src"); continue
        content=None; fp=None
        for e in [".tsx",".ts"]:
            c=src/f"{comp}{e}"
            if c.exists(): content=read_file(c); fp=c; break
        if not content:
            i=src/"index.ts"
            if i.exists(): content=read_file(i); fp=i
        if not content:
            for f in sorted(src.glob("*.tsx")):
                content=read_file(f); fp=f; break
        if not content: print("  [WARN] "+comp+": no file"); continue
        print(f"    [DEBUG mine_radix] Processing {comp}, content len={len(content)}", file=sys.stderr)
        debug_import = __import__("sys")
        props=extract_all(content)
        print(f"    [DEBUG mine_radix] extract_all returned {len(props)} props for {comp}", file=sys.stderr)
        nprops=extract_type(content,comp.title()+"Props")
        print(f"    [DEBUG mine_radix] extract_type returned {len(nprops)} props for {comp.title()+'Props'}", file=sys.stderr)
        for p in nprops:
            if p["name"] not in [x["name"] for x in props]: props.append(p)
        ev=get_events(comp); acc=get_access(comp.lower()); tag=TAGS.get(comp,"div")
        data={"meta":{"name":comp.title(),"source":"Radix UI","ver":"1.0.0","date":datetime.now().strftime("%Y-%m-%d"),"type":"web"},"sem":{"tag":tag,"container":False,"children":True,"role":comp.lower()},"props":props,"events":ev,"access":acc}
        WO.mkdir(parents=True,exist_ok=True)
        with open(WO/f"{comp.title()}_v2.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=2,ensure_ascii=False)
        print("  [OK] "+comp+": "+str(len(props))+"p "+str(len(ev))+"e")
        ext.append(comp)
        if str(fp) not in cp.get("processed",[]): cp.setdefault("processed",[]).append(str(fp))
        if comp not in cp.get("extracted",[]): cp.setdefault("extracted",[]).append(comp)
        save_cp(cp)
    return ext

def mine_konva():
    cp=load_cp(); ext=[]
    nc=read_file(KV/"Node.ts"); sc=read_file(KV/"Shape.ts"); cc=read_file(KV/"Container.ts")
    bn=extract_type(nc,"NodeConfig") if nc else []
    bs=extract_type(sc,"ShapeConfig") if sc else []
    bc=extract_type(cc,"ContainerConfig") if cc else []
    allb=bn+bs+bc; seen=set(); bp=[]
    for p in allb:
        if p["name"] not in seen: seen.add(p["name"]); bp.append(p)
    for p in bp:
        if p["name"]=="visible": p["default"]=True
        elif p["name"]=="listening": p["default"]=True
        elif p["name"]=="draggable": p["default"]=False
        elif p["name"]=="opacity": p["default"]=1
        elif p["name"]=="rotation": p["default"]=0
        p["css"]=CSS.get(p["name"],None); p["cat"]=cat(p["name"])
        if p["type"]=="number" and not p.get("constraints"): p["constraints"]={"min":0}
    for sn in DESIGN:
        if sn in cp.get("extracted",[]): print("  [SKIP] "+sn); ext.append(sn); continue
        f=KV/f"shapes/{sn}.ts"
        if not f.exists(): print("  [WARN] "+sn+": no file"); continue
        content=read_file(f)
        if not content: continue
        props=[p.copy() for p in bp]
        sp=extract_type(content,sn+"Config")
        for p in sp:
            if p["name"] not in [x["name"] for x in props]:
                p["css"]=CSS.get(p["name"],None); p["constraints"]={"min":0} if p["type"]=="number" else None
                p["cat"]=cat(p["name"])
                if p["name"]=="cornerRadius": p["default"]=0
                props.append(p)
        ev=[{"name":"click","params":["MouseEvent"]},{"name":"dblclick","params":["MouseEvent"]},{"name":"mousedown","params":["MouseEvent"]},{"name":"mouseup","params":["MouseEvent"]},{"name":"mouseenter","params":["MouseEvent"]},{"name":"mouseleave","params":["MouseEvent"]},{"name":"touchstart","params":["TouchEvent"]},{"name":"touchend","params":["TouchEvent"]},{"name":"dragstart","params":["DragEvent"]},{"name":"dragmove","params":["DragEvent"]},{"name":"dragend","params":["DragEvent"]},{"name":"transform","params":["Event"]}]
        caps={"freeform":sn=="Path","path":sn in ("Path","Line"),"corners":sn in ("Rect","Image","RegularPolygon"),"blend":True,"grad":True}
        data={"meta":{"name":sn,"source":"Konva.js","ver":"10.3.0","date":datetime.now().strftime("%Y-%m-%d"),"type":"design"},"props":props,"events":ev,"caps":caps}
        DO.mkdir(parents=True,exist_ok=True)
        with open(DO/f"{sn}_v2.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=2,ensure_ascii=False)
        print("  [OK] "+sn+": "+str(len(props))+"p "+str(len(ev))+"e")
        ext.append(sn)
        if str(f) not in cp.get("processed",[]): cp.setdefault("processed",[]).append(str(f))
        if sn not in cp.get("extracted",[]): cp.setdefault("extracted",[]).append(sn)
        save_cp(cp)
    return ext

def report(web,design):
    tw=0; ew=0
    for c in web:
        with open(WO/f"{c.title()}_v2.json","r",encoding="utf-8-sig") as f:
            d=json.load(f); tw+=len(d.get("props",[])); ew+=len(d.get("events",[]))
    td=0; ed=0
    for s in design:
        with open(DO/f"{s}_v2.json","r",encoding="utf-8-sig") as f:
            d=json.load(f); td+=len(d.get("props",[])); ed+=len(d.get("events",[]))
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rate=round((len(web)+len(design))/(len(WEB)+len(DESIGN))*100,1)
    lines=["="*60,"GCF - FULL MINING REPORT","="*60,"","Project: GCF","Date: "+now,"","--- WEB ---","Extracted: "+str(len(web))+"/"+str(len(WEB)),"Props: "+str(tw),"Events: "+str(ew),"","--- DESIGN ---","Extracted: "+str(len(design))+"/"+str(len(DESIGN)),"Props: "+str(td),"Events: "+str(ed),"","--- TOTALS ---","Elements: "+str(len(web)+len(design)),"Props: "+str(tw+td),"Events: "+str(ew+ed),"","--- STATUS ---","Result: "+("SUCCESS" if len(web)>=18 and len(design)>=10 else "PARTIAL"),"Rate: "+str(rate)+"%","","="*60,"END","="*60]
    RP.parent.mkdir(parents=True,exist_ok=True)
    open(RP,"w",encoding="utf-8").write("\n".join(lines))
    print("  [REPORT] saved")

if __name__=="__main__":
    print("="*60); print("  GCF - FULL MINER v3"); print("="*60); print()
    print("[1/3] Mining Radix UI..."); web=mine_radix(); print()
    print("[2/3] Mining Konva.js..."); design=mine_konva(); print()
    print("[3/3] Writing report..."); report(web,design); print()
    print("="*60); print("  RESULT: "+str(len(web))+"/"+str(len(WEB))+" + "+str(len(design))+"/"+str(len(DESIGN))); print("="*60)