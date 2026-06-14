#!/usr/bin/env python3
import os, re, json
from pathlib import Path
from datetime import datetime

BASE = Path("C:/Users/Administrator/Desktop/WebProject")
RADIX = BASE / "01-mines/web-mine/radix-ui/packages/react"
OUT = BASE / "03-gold-boxes/web-props"

def extract(content):
    props = []
    pat = r"interface\s+(\w+Props)\s*[^{]*\{([^}]+)\}"
    for m in re.finditer(pat, content, re.DOTALL):
        body = m.group(2)
        for p in re.finditer(r"(\w+)\??:\s*([^;]+);", body):
            nm, pt = p.group(1), p.group(2).strip()
            ui = "text_input"
            if "boolean" in pt: ui = "toggle"
            elif "number" in pt: ui = "slider"
            elif "|" in pt: ui = "select"
            props.append({"name":nm,"type":"enum" if "|" in pt else pt.split()[0],"required":"?" not in str(p.group()),"description":"","uiControl":ui})
    return props

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    n = 0
    for comp in sorted(RADIX.iterdir()):
        if not comp.is_dir(): continue
        src = comp / "src"
        if not src.exists(): continue
        for f in src.glob("*.tsx"):
            cnt = f.read_text(encoding="utf-8-sig",errors="ignore")
            props = extract(cnt)
            if props:
                nm = comp.name
                data = {"meta":{"name":nm,"source":"Radix UI","ver":"1.0.0","date":datetime.now().strftime("%Y-%m-%d"),"type":"web"},"props":props,"events":[]}
                json.dump(data,open(OUT / (nm+"_v2.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
                n += 1
                print("  "+nm+": "+str(len(props))+" props")
    print("Done. "+str(n)+" components")
if __name__=="__main__": main()
