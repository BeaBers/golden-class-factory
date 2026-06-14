#!/usr/bin/env python3
import os, json, datetime
from pathlib import Path
BASE = Path(r'C:\\Users\\Administrator\\Desktop\\WebProject')
WEB_DIR = BASE / '03-gold-boxes' / 'web-props'
DESIGN_DIR = BASE / '03-gold-boxes' / 'design-props'

WEB_DESC = {
    'disabled': 'Whether the component is disabled',
    'required': 'Whether the field is required',
    'readOnly': 'Whether the field is read-only',
    'value': 'The controlled value',
    'defaultValue': 'The initial value',
    'open': 'Whether the component is open/visible',
    'defaultOpen': 'Whether initially open',
    'modal': 'Whether the component is modal',
    'dir': 'Text direction: ltr or rtl',
    'orientation': 'Layout: horizontal or vertical',
    'loop': 'Whether navigation loops',
    'collapsible': 'Whether can be collapsed',
    'forceMount': 'Always mount in DOM',
    'className': 'CSS class name(s)',
    'style': 'Inline CSS styles',
    'children': 'Content of the component',
    'role': 'ARIA role',
    'tabIndex': 'Tab order index',
}

UI_MAP = {
    'boolean': 'toggle', 'string': 'text_input', 'number': 'number_input',
    'integer': 'number_input',
}

CSS_EQ = {
    'x': 'left', 'y': 'top', 'width': 'width', 'height': 'height',
    'opacity': 'opacity', 'rotation': 'transform: rotate()',
    'scaleX': 'transform: scaleX()', 'scaleY': 'transform: scaleY()',
    'fill': 'background-color', 'stroke': 'border-color',
    'strokeWidth': 'border-width', 'cornerRadius': 'border-radius',
    'shadowColor': 'box-shadow color', 'shadowBlur': 'box-shadow blur radius',
    'shadowOffsetX': 'box-shadow offset-x',
    'shadowOffsetY': 'box-shadow offset-y',
    'shadowOpacity': 'box-shadow opacity',
    'fontSize': 'font-size', 'fontFamily': 'font-family',
    'fontStyle': 'font-style', 'fontWeight': 'font-weight',
    'textDecoration': 'text-decoration', 'align': 'text-align',
    'verticalAlign': 'vertical-align', 'lineHeight': 'line-height',
    'letterSpacing': 'letter-spacing', 'padding': 'padding',
    'visible': 'visibility', 'draggable': 'N/A',
}

def infer_ui(ptype, name):
    t = (ptype or '').lower().strip()
    n = name.lower()
    if 'color' in n or 'colour' in n: return 'color_picker'
    if n in ['fill','stroke','shadowColor']: return 'color_picker'
    if t in ['boolean','bool']: return 'toggle'
    if n in ['visible','disabled','required','readOnly','modal','loop','collapsible','draggable','checked','open']: return 'toggle'
    if n in ['opacity','cornerRadius','radius','fontSize','lineHeight','rotation','angle','strokeWidth']: return 'slider'
    if t in ['number','integer']: return 'number_input'
    if t == 'string': return 'select' if n in ['dir','orientation','type','role','align'] else 'text_input'
    if '|' in t: return 'select'
    if 'event' in t or n.startswith('on'): return 'event_handler'
    if t.startswith('('): return 'code_editor'
    if 'react' in t.lower(): return 'element_picker'
    if t.startswith('array') or t.startswith('['): return 'array_input'
    if t in ['object','any']: return 'json_editor'
    return 'text_input'

def gen_desc(prop, cat):
    name = prop.get('name','')
    ptype = prop.get('type','')
    desc = prop.get('description','')
    if desc and len(desc) > 5: return desc
    if cat == 'web' and name in WEB_DESC: return WEB_DESC[name]
    if cat == 'design' and name in DESIGN_DESC: return DESIGN_DESC[name]
    clean = name.replace('_',' ').replace('-',' ').replace('aria','ARIA').replace('on','')
    if ptype and ptype != 'any': return f'{clean} ({ptype})'
    return f'{clean} property'

def process_all():
    modified_count = 0
    total_props = 0
    for cat, path in [('web', WEB_DIR), ('design', DESIGN_DIR)]:
        for fname in sorted(os.listdir(path)):
            fp = path / fname
            with open(fp, 'r', encoding='utf-8-sig') as f: data = json.load(f)
            props = data.get('props', [])
            changed = False
            for p in props:
                name = p.get('name','')
                ptype = p.get('type','')
                if not p.get('description','').strip() or len(p.get('description','').strip()) < 5:
                    p['description'] = gen_desc(p, cat)
                    changed = True
                if not p.get('uiControl','').strip():
                    p['uiControl'] = infer_ui(ptype, name)
                    changed = True
                if cat == 'design':
                    cur = p.get('cssEquivalent','')
                    if not cur or cur.strip() == '':
                        p['cssEquivalent'] = CSS_EQ.get(name, '')
                        changed = True
            if changed:
                data['props'] = props
                with open(fp, 'w', encoding='utf-8') as f: json.dump(data, f, indent=2, ensure_ascii=False)
                modified_count += 1
            total_props += len(props)
    print(f'Modified: {modified_count} files')
    print(f'Total props: {total_props}')
    return total_props

total = process_all()
print(f'Done. Total props: {total}')
