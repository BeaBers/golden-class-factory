#!/usr/bin/env python3
import json, os
from pathlib import Path

BASE = Path("C:/Users/Administrator/Desktop/WebProject")

def check(fp):
    issues = []
    sz = os.path.getsize(fp)
    if sz < 1000: issues.append("size<1KB")
    with open(fp, "r", encoding="utf-8") as f: data = json.load(f)
    props = data.get("props", [])
    if len(props) == 0: issues.append("0 props")
    nd = sum(1 for p in props if not p.get("description","").strip())
    nu = sum(1 for p in props if not p.get("uiControl","").strip())
    if nd > 0: issues.append(f"{nd} no_desc")
    if nu > 0: issues.append(f"{nu} no_ui")
    return issues

def main():
    total = perfect = 0
    for cat in ["web-props", "design-props"]:
        for f in sorted((BASE / "03-gold-boxes" / cat).glob("*.json")):
            total += 1
            issues = check(f)
            if issues: print("  " + f.name + ": " + str(issues))
            else: perfect += 1
    print(f"Total: {total}, Perfect: {perfect} ({round(perfect/total*100,1)}%)")
if __name__ == "__main__": main()
