#!/usr/bin/env python3
import json, os
from pathlib import Path

BASE = Path("C:/Users/Administrator/Desktop/WebProject")

def clean(v):
    if isinstance(v, str): return v.strip().lstrip('\ufeff')
    if isinstance(v, dict): return {k.strip(): clean(v) for k, v in v.items()}
    if isinstance(v, list): return [clean(i) for i in v]
    return v

def main():
    cleaned = 0
    for cat in ["web-props", "design-props"]:
        d = BASE / "03-gold-boxes" / cat
        for f in sorted(d.glob("*.json")):
            with open(f, "r", encoding="utf-8-sig") as fh: data = json.load(fh)
            clean_data = clean(data)
            with open(f, "w", encoding="utf-8") as fh: json.dump(clean_data, fh, indent=2, ensure_ascii=False)
            cleaned += 1
            print("  " + f.name)
    print(f"Cleaned {cleaned} files")
if __name__ == "__main__": main()
