import json, os, sys

def analyze(data, name):
    print(f"\n=== {name} ===")
    print(f"Props: {len(data['props'])}")
    types = {}
    for p in data["props"]:
        types[p["type"]] = types.get(p["type"], 0) + 1
    print(f"Types: {types}")
    cats = {}
    for p in data["props"]:
        cats[p["category"]] = cats.get(p["category"], 0) + 1
    print(f"Categories: {cats}")
    ctrls = {}
    for p in data["props"]:
        ctrls[p.get("uiControl","?")] = ctrls.get(p.get("uiControl","?"), 0) + 1
    print(f"Controls: {ctrls}")
    no_css = [p["name"] for p in data["props"] if not p.get("css")]
    print(f"No CSS ({len(no_css)}): {no_css[:10]}...")
    has_av = [p["name"] for p in data["props"] if p.get("allowedValues")]
    print(f"AllowedValues: {has_av}")
    has_def = [p["name"] for p in data["props"] if p.get("default") is not None]
    print(f"Defaults: {has_def}")
    has_con = [p["name"] for p in data["props"] if p.get("constraints")]
    print(f"Constraints: {has_con}")
    fallback = [p["name"] for p in data["props"] if chr(1582) in p.get("description","")]
    if fallback: print(f"Fallback descriptions: {fallback}")

with open("C:/Users/Administrator/Desktop/WebProject/03-gold-boxes/web-props/Select_v5.json", "r", encoding="utf-8-sig") as f:
    web = json.load(f)
with open("C:/Users/Administrator/Desktop/WebProject/03-gold-boxes/design-props/Text_v5.json", "r", encoding="utf-8-sig") as f:
    design = json.load(f)

analyze(web, "Select_v5 (Web)")
analyze(design, "Text_v5 (Design)")
