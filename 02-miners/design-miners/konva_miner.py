#!/usr/bin/env python3
import os, re, json
from pathlib import Path
from datetime import datetime

BASE = Path("C:/Users/Administrator/Desktop/WebProject")
SHAPES = BASE / "01-mines/design-mine/konva/src/shapes"
OUT = BASE / "03-gold-boxes/design-props"

def extract(content):
    props = []
    pat = r"(?:interface|type)\s+(\w+Config\w*)\s*(?:extends\s+[^{]+)?\s*(?:=|)?\s*\{([^}]+)\}"
    for m in re.finditer(pat, content, re.DOTALL):
        body = m.group(2)
        for p in re.finditer(r"(\w+)\??:\s*([^;]+);", body):
            nm, pt = p.group(1), p.group(2).strip()
            ui = "text_input"
            if "boolean" in pt: ui = "toggle"
            elif "number" in pt: ui = "slider"
            elif "|" in pt: ui = "select"
            props.append({"name":nm,"type":"enum" if "|" in pt else pt.split()[0],"required":"?" not in str(p.group()),"description":"","uiControl":ui,"cssEquivalent":""})
    return props

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    n = 0
    for f in sorted(SHAPES.glob("*.ts")):
        cnt = f.read_text(encoding="utf-8-sig",errors="ignore")
        props = extract(cnt)
        if props:
            nm = f.stem
            data = {"meta":{"name":nm,"source":"Konva.js","ver":"10.3.0","date":datetime.now().strftime("%Y-%m-%d"),"type":"design"},"props":props,"events":[]}
            json.dump(data,open(OUT / (nm+"_v2.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
            n += 1
            print("  "+nm+": "+str(len(props))+" props")
    print("Done. "+str(n)+" shapes")
if __name__=="__main__": main()
