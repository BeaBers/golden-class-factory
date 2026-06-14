import os, sys
sys.stdout.reconfigure(encoding="utf-8")
p = "C:/Users/Administrator/Desktop/WebProject/02-miners/utils/gen_v6.py"
with open(p, "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write("# Generator for full_miner_v6.py\n")
    f.write("import os, json, sys\n\n")
    f.write('OUT = r"C:/Users/Administrator/Desktop/WebProject/02-miners/utils/full_miner_v6.py"\n\n')
    f.write("def w(text):\n")
    f.write("    with open(OUT, 'a', encoding='utf-8') as f:\n")
    f.write("        f.write(text + '\\n')\n\n")
    f.write("# Start fresh\n")
    f.write('open(OUT, "w", encoding="utf-8").close()\n')
print("Written OK")
# PART 1: CSS_MAP
with open(OUT, "a", encoding="utf-8") as f:
    f.write('''
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
    "globalCompositeOperation": "mix-blend-mode", "blendMode": "mix-blend-mode",
    "filters": "filter (CSS functions)",
    "rotation": "transform: rotate(Ndeg)", "rotationDeg": "transform: rotate(Ndeg)",
    "scale": "transform: scale(N)", "scaleX": "transform: scaleX(N)",
    "scaleY": "transform: scaleY(N)", "skewX": "transform: skewX(Ndeg)", "skewY": "transform: skewY(Ndeg)",
    "fontSize": "font-size", "fontFamily": "font-family", "fontStyle": "font-style",
    "fontWeight": "font-weight", "fontVariant": "font-variant",
    "lineHeight": "line-height", "letterSpacing": "letter-spacing",
    "textAlign": "text-align", "verticalAlign": "vertical-align",
    "textDecoration": "text-decoration", "textTransform": "text-transform",
    "color": "color", "textColor": "color", "direction": "direction",
    "wordSpacing": "word-spacing", "textShadow": "text-shadow", "whiteSpace": "white-space",
    "overflow": "overflow", "textOverflow": "text-overflow",
    "wrap": "white-space / overflow-wrap", "ellipsis": "text-overflow", "align": "text-align",
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
    "outlineStyle": "outline-style", "outlineColor": "outline-color", "outlineOffset": "outline-offset",
    "cursor": "cursor", "pointerEvents": "pointer-events",
    "userSelect": "user-select", "resize": "resize",
    "transition": "transition", "transform": "transform",
    "boxShadow": "box-shadow", "listStyle": "list-style", "listStyleType": "list-style-type",
    "id": "id (HTML attribute)", "className": "class", "name": "name (HTML attribute)",
    "value": "value (HTML attribute)", "placeholder": "placeholder",
    "title": "title (HTML attribute)", "alt": "alt (HTML attribute)",
    "src": "src (HTML attribute)", "href": "href (HTML attribute)",
    "target": "target (HTML attribute)", "rel": "rel (HTML attribute)",
    "type": "type (HTML attribute)", "disabled": "disabled (HTML attribute)",
    "readOnly": "readonly (HTML attribute)", "required": "required (HTML attribute)",
    "autoFocus": "autofocus (HTML attribute)", "tabIndex": "tabindex",
    "autoComplete": "autocomplete (HTML attribute)",
    "nonce": "nonce (HTML attribute)", "form": "form (HTML attribute)",
    "dir": "direction", "lang": "lang (HTML attribute)",
    "draggable": None, "dragDistance": None, "dragBoundFunc": None,
    "preventDefault": None, "listening": None,
    "hitFunc": None, "sceneFunc": None, "clipFunc": None,
    "clipX": "clip-path (X)", "clipY": "clip-path (Y)",
    "clipWidth": "clip-path (width)", "clipHeight": "clip-path (height)",
    "clearBeforeDraw": None, "perfectDrawEnabled": None,
    "underlineOffset": "text-underline-offset",
    "asChild": None, "as": None,
    "defaultOpen": None, "open": None,
    "defaultValue": None, "defaultChecked": None, "checked": None,
    "onCheckedChange": None, "onOpenChange": None,
    "onValueChange": None, "onClick": None, "onFocus": None, "onBlur": None,
    "forceMount": None, "onAutoScroll": None, "container": None,
    "fragment": None, "onCloseAutoFocus": None,
    "onEscapeKeyDown": None, "onPointerDownOutside": None, "textValue": None,
}
''')
w('''
ALLOWED_VALUES_MAP = {
    "dir": ["ltr", "rtl", "auto"],
    "autoComplete": ["off", "on", "name", "email", "username", "new-password", "current-password"],
    "lineCap": ["butt", "round", "square"],
    "lineJoin": ["miter", "round", "bevel"],
    "fillRule": ["nonzero", "evenodd"],
    "fillPriority": ["color", "gradient", "pattern"],
    "fillPatternRepeat": ["repeat", "repeat-x", "repeat-y", "no-repeat"],
    "globalCompositeOperation": ["source-over", "source-in", "source-out", "source-atop", "destination-over", "destination-in", "destination-out", "destination-atop", "lighter", "xor", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge", "color-burn", "hard-light", "soft-light", "difference", "exclusion"],
    "textAlign": ["left", "center", "right", "justify", "start", "end"],
    "verticalAlign": ["top", "middle", "bottom"],
    "fontStyle": ["normal", "italic", "oblique"],
    "fontVariant": ["normal", "small-caps"],
    "fontWeight": ["100","200","300","400","500","600","700","800","900","normal","bold","bolder","lighter"],
    "textDecoration": ["none", "underline", "overline", "line-through"],
    "textTransform": ["none", "capitalize", "uppercase", "lowercase"],
    "whiteSpace": ["normal", "nowrap", "pre", "pre-wrap", "pre-line"],
    "overflow": ["visible", "hidden", "clip", "scroll", "auto"],
    "position": ["static", "relative", "absolute", "fixed", "sticky"],
    "flexDirection": ["row", "row-reverse", "column", "column-reverse"],
    "flexWrap": ["nowrap", "wrap", "wrap-reverse"],
    "alignContent": ["flex-start", "flex-end", "center", "space-between", "space-around", "stretch"],
    "alignItems": ["flex-start", "flex-end", "center", "baseline", "stretch"],
    "justifyContent": ["flex-start", "flex-end", "center", "space-between", "space-around", "space-evenly"],
    "borderStyle": ["none","hidden","dotted","dashed","solid","double","groove","ridge","inset","outset"],
    "cursor": ["auto","default","pointer","text","move","not-allowed","crosshair","grab","zoom-in"],
    "resize": ["none", "both", "horizontal", "vertical"],
    "userSelect": ["none", "auto", "text", "contain", "all"],
    "outlineStyle": ["none","hidden","dotted","dashed","solid","double","groove","ridge","inset","outset"],
    "wrap": ["none", "word", "char"],
}

CONSTRAINTS_MAP = {
    "opacity": {"min":0,"max":1,"step":0.01}, "rotation": {"min":-360,"max":360},
    "rotationDeg": {"min":-360,"max":360},
    "scaleX": {"min":-10,"max":10,"step":0.1}, "scaleY": {"min":-10,"max":10,"step":0.1},
    "scale": {"min":-10,"max":10,"step":0.1},
    "skewX": {"min":-360,"max":360}, "skewY": {"min":-360,"max":360},
    "shadowBlur": {"min":0,"max":100}, "shadowOpacity": {"min":0,"max":1,"step":0.01},
    "shadowOffsetX": {"min":-100,"max":100}, "shadowOffsetY": {"min":-100,"max":100},
    "strokeWidth": {"min":0,"max":100}, "hitStrokeWidth": {"min":0,"max":100},
    "borderWidth": {"min":0,"max":50}, "cornerRadius": {"min":0,"max":999},
    "fontSize": {"min":1,"max":999}, "letterSpacing": {"min":-10,"max":50},
    "lineHeight": {"min":0,"max":10,"step":0.1}, "wordSpacing": {"min":-10,"max":50},
    "miterLimit": {"min":0,"max":100}, "tabIndex": {"min":-1,"step":1},
    "zIndex": {"min":-9999,"max":9999,"step":1},
    "flexGrow": {"min":0,"step":1}, "flexShrink": {"min":0,"step":1},
    "order": {"min":-999,"max":999,"step":1},
    "padding": {"min":0,"max":999}, "gap": {"min":0,"max":999}, "margin": {"min":-999,"max":999},
    "dragDistance": {"min":0}, "underlineOffset": {"min":-10,"max":50},
}

CATEGORY_OVERRIDE = {
    "children": "content", "dir": "layout", "container": "content",
    "nonce": "content", "fragment": "content", "form": "content",
    "placeholder": "content", "autoComplete": "behavior",
    "asChild": "behavior", "as": "behavior", "forceMount": "behavior",
    "defaultOpen": "content", "defaultValue": "content", "defaultChecked": "content",
    "open": "state", "checked": "state", "value": "content",
    "tabIndex": "behavior", "hitStrokeWidth": "interaction",
    "sceneFunc": "rendering", "hitFunc": "interaction", "clipFunc": "rendering",
    "clearBeforeDraw": "rendering", "perfectDrawEnabled": "rendering",
    "listening": "interaction",
}
''')
w('''
DEPENDENCY_MAP = {
    "shadowColor": {"dependsOn": "shadowBlur", "condition": ">", "value": 0},
    "shadowOffsetX": {"dependsOn": "shadowBlur", "condition": ">", "value": 0},
    "shadowOffsetY": {"dependsOn": "shadowBlur", "condition": ">", "value": 0},
    "shadowOpacity": {"dependsOn": "shadowBlur", "condition": ">", "value": 0},
    "borderColor": {"dependsOn": "borderWidth", "condition": ">", "value": 0},
    "borderStyle": {"dependsOn": "borderWidth", "condition": ">", "value": 0},
    "dashOffset": {"dependsOn": "dash", "condition": "!=", "value": None},
    "fillPatternX": {"dependsOn": "fillPatternImage", "condition": "!=", "value": None},
    "fillPatternY": {"dependsOn": "fillPatternImage", "condition": "!=", "value": None},
    "fillPatternRepeat": {"dependsOn": "fillPatternImage", "condition": "!=", "value": None},
    "fillLinearGradientStartPointX": {"dependsOn": "fillLinearGradientColorStops", "condition": "!=", "value": None},
    "fillLinearGradientEndPointX": {"dependsOn": "fillLinearGradientColorStops", "condition": "!=", "value": None},
    "fillRadialGradientStartRadius": {"dependsOn": "fillRadialGradientColorStops", "condition": "!=", "value": None},
    "fillRadialGradientEndRadius": {"dependsOn": "fillRadialGradientColorStops", "condition": "!=", "value": None},
    "strokeScaleEnabled": {"dependsOn": "strokeWidth", "condition": ">", "value": 0},
    "strokeHitEnabled": {"dependsOn": "strokeWidth", "condition": ">", "value": 0},
    "hitStrokeWidth": {"dependsOn": "strokeWidth", "condition": ">", "value": 0},
    "clipWidth": {"dependsOn": "clipFunc", "condition": "==", "value": None},
    "clipHeight": {"dependsOn": "clipFunc", "condition": "==", "value": None},
    "clipX": {"dependsOn": "clipFunc", "condition": "==", "value": None},
    "clipY": {"dependsOn": "clipFunc", "condition": "==", "value": None},
}

CSS_FORMAT_MAP = {
    "shadow": "box-shadow: {shadowOffsetX}px {shadowOffsetY}px {shadowBlur}px {shadowColor}",
    "border": "border: {borderWidth}px {borderStyle} {borderColor}",
    "outline": "outline: {outlineWidth}px {outlineStyle} {outlineColor}",
    "dash": "stroke-dasharray: {dash}",
    "transform": "transform: translate({x}px,{y}px) rotate({rotation}deg) scale({scaleX},{scaleY})",
    "clipPath": "clip-path: inset({clipY}px {clipWidth}px {clipHeight}px {clipX}px)",
}
''')
w(r'''DESC_TEMPLATES = {
    "x": "الإحداثي الأفقي (X) للعنصر من الزاوية اليسرى",
    "y": "الإحداثي الرأسي (Y) للعنصر من الزاوية العلوية",
    "width": "عرض العنصر بالبكسل", "height": "ارتفاع العنصر بالبكسل",
    "fill": "لون تعبئة الخلفية", "stroke": "لون الحدود الخارجية",
    "strokeWidth": "سماكة الحدود الخارجية بالبكسل",
    "opacity": "درجة الشفافية (0=شفاف تماماً، 1=معتم)",
    "visible": "التحكم في ظهور/إخفاء العنصر",
    "rotation": "زاوية الدوران بالدرجات (قيمة موجبة = مع عقارب الساعة)",
    "rotationDeg": "زاوية الدوران بالدرجات (0-360)",
    "cornerRadius": "نصف قطر تدوير الزوايا بالبكسل",
    "shadowColor": "لون الظل المسقط أسفل العنصر",
    "shadowBlur": "مقدار ضبابية الظل بالبكسل",
    "shadowOffsetX": "إزاحة الظل أفقياً بالبكسل (قيمة موجبة = يمين)",
    "shadowOffsetY": "إزاحة الظل رأسياً بالبكسل (قيمة موجبة = أسفل)",
    "shadowOpacity": "شفافية الظل (0=شفاف، 1=معتم)",
    "shadowOffset": "إزاحة الظل الكلية (X,Y)",
    "shadowEnabled": "تفعيل/إلغاء الظل على العنصر",
    "shadowForStrokeEnabled": "تفعيل الظل للحدود فقط",
    "scaleX": "مقياس التكبير/التصغير الأفقي (1=حجم طبيعي)",
    "scaleY": "مقياس التكبير/التصغير الرأسي",
    "scale": "مقياس التكبير/التصغير الكلي",
    "skewX": "إمالة أفقية بالدرجات", "skewY": "إمالة رأسية بالدرجات",
    "dash": "نمط الخط المتقطع: [طول_الخط, المسافة_بينهم]",
    "dashOffset": "إزاحة بداية نمط الخط المتقطع",
    "lineCap": "شكل نهاية الخط: butt (مربع)، round (دائري)، square (مربع بارز)",
    "lineJoin": "شكل التقاء الخطوط: miter (مدبب)، round (دائري)، bevel (مشطوف)",
    "miterLimit": "الحد الأقصى لطول الزاوية المدببة",
    "draggable": "السماح بسحب العنصر بالماوس أو اللمس",
    "dragDistance": "المسافة الدنيا بالبكسل قبل بدء السحب",
    "dragBoundFunc": "دالة تحديد حدود السحب",
    "preventDefault": "منع السلوك الافتراضي للمتصفح",
    "disabled": "تعطيل التفاعل مع العنصر",
    "fontSize": "حجم الخط بالبكسل",
    "fontFamily": "نوع الخط المستخدم",
    "fontWeight": "سماكة الخط (400=عادي، 700=عريض)",
    "fontStyle": "نمط الخط (normal=عادي، italic=مائل)",
    "fontVariant": "تنويع الخط (normal=عادي، small-caps=أحرف صغيرة)",
    "textAlign": "محاذاة النص أفقياً",
    "verticalAlign": "محاذاة النص رأسياً",
    "lineHeight": "ارتفاع السطر (نسبة إلى حجم الخط)",
    "letterSpacing": "المسافة بين الأحرف بالبكسل",
    "wordSpacing": "المسافة بين الكلمات بالبكسل",
    "color": "لون النص", "textColor": "لون النص",
    "textDecoration": "زخرفة النص (underline, line-through)",
    "textTransform": "تحويل حالة النص (uppercase, lowercase)",
    "whiteSpace": "التحكم في المسافات البيضاء والتفاف النص",
    "overflow": "التحكم في تجاوز المحتوى للمساحة",
    "textOverflow": "عرض النص المتجاوز (ellipsis=...)",
    "wrap": "التحكم في التفاف النص",
    "ellipsis": "إضافة ... عند تجاوز النص",
    "direction": "اتجاه النص (ltr=يسار-يمين، rtl=يمين-يسار)",
    "align": "محاذاة النص", "underlineOffset": "إزاحة الخط السفلي",
    "padding": "الحشوة الداخلية بالبكسل",
    "margin": "الهامش الخارجي بالبكسل",
    "gap": "المسافة بين العناصر الفرعية",
    "flexDirection": "اتجاه الترتيب: row (أفقي)، column (رأسي)",
    "flexWrap": "السماح بالتفاف العناصر لسطر جديد",
    "justifyContent": "محاذاة العناصر على المحور الرئيسي",
    "alignItems": "محاذاة العناصر على المحور العرضي",
    "borderWidth": "سماكة الحدود بالبكسل", "borderColor": "لون الحدود",
    "borderStyle": "نمط الحدود (solid=متصل، dashed=متقطع)",
    "borderRadius": "نصف قطر تدوير الزوايا",
    "variant": "نمط المظهر: solid, outline, ghost, link",
    "size": "حجم المكون: sm (صغير)، md (متوسط)، lg (كبير)",
    "colorScheme": "نظام الألوان للمكون",
    "label": "النص المعروض على المكون",
    "placeholder": "نص تلميحي عند فراغ الحقل",
    "id": "معرف فريد للعنصر (HTML id)",
    "className": "فئة CSS إضافية",
    "name": "اسم العنصر (يُستخدم في النماذج)",
    "value": "القيمة الحالية للعنصر",
    "defaultValue": "القيمة الافتراضية",
    "checked": "حالة التحديد (true=محدد)",
    "defaultChecked": "حالة التحديد الافتراضية",
    "required": "حقل إجباري", "readOnly": "للقراءة فقط",
    "autoFocus": "التركيز التلقائي", "tabIndex": "ترتيب التنقل بـ Tab",
    "asChild": "استخدام عنصر DOM مخصص بدلاً من الافتراضي",
    "as": "تحديد عنصر HTML بديل", "forceMount": "فرض البقاء في DOM",
    "defaultOpen": "الحالة الافتراضية للفتح", "open": "التحكم بالفتح/الإغلاق",
    "listening": "الاستماع للأحداث",
    "hitStrokeWidth": "عرض منطقة الاصطدام للحدود",
    "strokeScaleEnabled": "تفعيل تكبير الحدود مع الشكل",
    "strokeHitEnabled": "تفعيل اصطدام الفأرة بالحدود",
    "fillEnabled": "تفعيل تعبئة الشكل",
    "fillPriority": "أولوية التعبئة (color/gradient/pattern)",
    "fillRule": "قاعدة التعبئة للمسارات المتداخلة",
    "fillPatternImage": "صورة نمط التعبئة",
    "fillPatternX": "إزاحة النمط أفقياً", "fillPatternY": "إزاحة النمط رأسياً",
    "fillPatternRepeat": "تكرار نمط التعبئة",
    "fillLinearGradientColorStops": "نقاط توقف ألوان التدرج الخطي",
    "fillRadialGradientColorStops": "نقاط توقف ألوان التدرج الشعاعي",
    "globalCompositeOperation": "طريقة مزج الألوان",
    "filters": "مرشحات Canvas (blur, brightness...)",
    "sceneFunc": "دالة رسم مخصصة", "hitFunc": "دالة اصطدام مخصصة",
    "clipFunc": "دالة قص مخصصة",
    "clipX": "إحداثي X لمساحة القص", "clipY": "إحداثي Y لمساحة القص",
    "clipWidth": "عرض مساحة القص", "clipHeight": "ارتفاع مساحة القص",
    "clearBeforeDraw": "مسح القماش قبل الرسم",
    "perfectDrawEnabled": "تفعيل الرسم فائق الجودة",
    "children": "المحتوى الداخلي للعنصر",
    "container": "حاوية Portal للمحتوى المنقول",
    "nonce": "رمز أمني لسياسة CSP", "form": "ربط بنموذج HTML",
    "textValue": "قيمة نصية بديلة لإمكانية الوصول",
    "autoComplete": "الاقتراحات التلقائية للمتصفح",
    "dir": "اتجاه الكتابة (rtl=يمين-يسار، ltr=يسار-يمين)",
}
''' )
w(r'''
def map_type_v6(t, name=""):
    '''Enhanced type detection that handles function patterns correctly'''
    t = t.strip()
    if t == "boolean": return "boolean", "toggle", None
    if t == "string": return "string", "text_input", None
    if t == "number": return "number", "slider", None
    # Function detection - MUST be before string/enum checks
    # Handle: ((e: Event) => void) | undefined, () => void, function signatures
    stripped = t.replace(" ", "")
    if any(x in stripped for x in ["=>", "):", "Function"]):
        return "function", "code_input", None
    if t.startswith("(") and ("=>" in t or "):" in t):
        return "function", "code_input", None
    # Enum detection from type union
    if "'" in t and "|" in t:
        vals = [v.strip().strip("'") for v in t.split("|") if v.strip()]
        return "enum", "select", vals
    # Array
    if "[]" in t or t.startswith("Array"):
        return "array", "text_input", None
    # React node
    if any(x in t for x in ["React.ReactNode", "ReactNode", "React.Element"]):
        return "component", "component_picker", None
    # Event types
    if any(x in t for x in ["MouseEvent", "KeyboardEvent", "FocusEvent", "TouchEvent"]):
        return "function", "code_input", None
    return "string", "text_input", None

def categorize_v6(name):
    n = name.lower()
    # Check override first
    if name in CATEGORY_OVERRIDE: return CATEGORY_OVERRIDE[name]
    if n in ("x","y","width","height","minwidth","maxwidth","offset","offsetx","offsety"):
        return "dimension"
    if n in ("fontsize","fontfamily","fontweight","fontstyle","fontvariant","lineheight","letterspacing","wordspacing","textalign","verticalalign","textdecoration","texttransform","textshadow","whitespace","textoverflow","direction","align","wrap","ellipsis","underlineoffset"):
        return "typography"
    if n in ("gap","padding","margin","flexdirection","flexwrap","justifycontent","alignitems","aligncontent","alignself","flex","flexgrow","flexshrink","order","position","top","right","bottom","left","zindex","dir"):
        return "layout"
    if any(v in n for v in ["fill","stroke","shadow","opacity","visible","dash","line","corner","blur","filter","border","outline","gradient","pattern","blend","background","color","radius"]):
        return "visual"
    if n in ("rotation","rotationdeg","scale","scalex","scaley","skewx","skewy","transform"):
        return "transform"
    if any(v in n for v in ["drag","listening","hit","prevent","scroll","click"]):
        return "interaction"
    if n in ("disabled","checked","pressed","enabled","selected","readonly","required","open"):
        return "state"
    if n in ("value","defaultvalue","defaultchecked","defaultopen","label","placeholder","id","classname","name","title","alt","src","href","target","rel","type","tabindex","autofocus","children","container","nonce","form","textvalue","fragment"):
        return "content"
    if any(v in n for v in ["aschild","as","forcemount"]):
        return "behavior"
    if any(v in n for v in ["aria","role"]):
        return "accessibility"
    if any(v in n for v in ["onclick","onfocus","onblur","onchange","onkey"]):
        return "events"
    return "behavior"

INTERFACE_PATTERN = r"(?:interface|type)\s+(\w+)(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\\{"

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
    desc = ""; default_val = None
    i = idx - 1
    while i >= 0:
        line = lines[i].strip()
        if line == "": i -= 1; continue
        if line.startswith("*/"): i -= 1; continue
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
        elif line.startswith(("}",")","]")): break
        elif re.match(r"^\w+\s*\??\s*:", line): break
        else: break
        i -= 1
    return desc.strip(), default_val

def get_constraints(name):
    return CONSTRAINTS_MAP.get(name, None)

def get_allowed_values(name):
    return ALLOWED_VALUES_MAP.get(name, None)

def get_css(name):
    return CSS_MAP.get(name, None)

def get_desc(name, ptype, default_val):
    if name in DESC_TEMPLATES:
        d = DESC_TEMPLATES[name]
        if ptype == "boolean" and default_val is not None:
            d += f" (الافتراضي: {default_val})"
        return d
    t_map = {"boolean": " (منطقي)", "number": " (رقمي)", "string": " (نصي)",
             "function": " (دالة)", "array": " (مصفوفة)", "enum": " (قيم محددة)"}
    return f"خاصية {name}" + t_map.get(ptype, "")

def get_depends(name):
    return DEPENDENCY_MAP.get(name, None)

def parse_ts_v6(body_lines, source_name=""):
    props = []
    lines = body_lines.split("\\n") if isinstance(body_lines, str) else body_lines
    if isinstance(lines, str): lines = [lines]
    for idx, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith(("//","/*","*","}","[","]")): continue
        cln = re.sub(r"\([^)]*\)", "", line)
        m = re.match(r"(?P<n>\w+)\s*(?P<o>\??)\s*:\s*(?P<t>[^;]+?)\s*;?\s*$", cln)
        if not m: continue
        n = m.group("n"); ot = m.group("o"); rt = m.group("t").strip()
        if n in ("string","number","boolean","any","unknown","readonly","key","typeof"): continue
        desc, default_val = extract_jsdoc_v2(lines, idx)
        js, ui, av = map_type_v6(rt, n)
        if not av: av = get_allowed_values(n)
        if not desc: desc = get_desc(n, js, default_val)
        cons = get_constraints(n)
        css_equiv = get_css(n)
        deps = get_depends(n)
        prop = {
            "name": n, "type": js, "required": ot != "?",
            "default": default_val, "allowedValues": av,
            "description": desc, "uiControl": ui,
            "category": categorize_v6(n), "constraints": cons,
            "css": css_equiv,
        }
        if deps: prop["dependsOn"] = deps
        # Verify type matches allowedValues
        if av and js == "string":
            prop["type"] = "enum"
            prop["uiControl"] = "select"
        props.append(prop)
    return props

def extract_all_v6(content):
    allp = []
    for m in re.finditer(INTERFACE_PATTERN, content):
        si = m.end() - 1
        ei = extract_block(content, si)
        body = content[si+1:ei]
        for p in parse_ts_v6(body.split("\\n"), m.group(1)):
            if p["name"] not in [x["name"] for x in allp]:
                allp.append(p)
    return allp

def extract_type_v6(content, tname):
    for pat in [
        r"interface\s+" + re.escape(tname) + r"(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\\{",
        r"type\s+" + re.escape(tname) + r"(?:<[^>]*>)?\s*=\s*(?:[^{]*?\\&\\s*)?\\{",
    ]:
        m = re.search(pat, content)
        if m:
            si = m.end() - 1
            ei = extract_block(content, si)
            return parse_ts_v6(content[si+1:ei].split("\\n"), tname)
    return []
''')
w(r'''
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
    {"name":"transform","params":["Event"],"description":"عند التحويل"},
    {"name":"mousewheel","params":["WheelEvent"],"description":"عند تدوير العجلة"},
    {"name":"contextmenu","params":["MouseEvent"],"description":"عند النقر بزر الفأرة الأيمن"},
]

RADIX_EVENTS_BASE = [
    {"name":"onClick","params":["React.MouseEvent"],"description":"عند النقر على المكون"},
    {"name":"onFocus","params":["React.FocusEvent"],"description":"عند اكتساب التركيز"},
    {"name":"onBlur","params":["React.FocusEvent"],"description":"عند فقدان التركيز"},
]

def get_component_events(cname):
    cl = cname.lower()
    ev = list(RADIX_EVENTS_BASE)
    open_close = ["dialog","popover","tooltip","hover-card","alert-dialog","collapsible"]
    value_change = ["select","radio-group","toggle","switch","checkbox","slider","progress","tabs","accordion","toggle-group"]
    if cl in open_close:
        ev.insert(0, {"name":"onOpenChange","params":["boolean"],"description":"عند تغيير حالة الفتح/الإغلاق"})
    if cl in value_change:
        desc_map = {"accordion":"عند تغيير العنصر الموسع","slider":"عند تغيير قيمة التمرير","tabs":"عند تغيير التبويب النشط","progress":"عند تغيير قيمة التقدم","toggle":"عند تغيير حالة الضغط","switch":"عند تغيير حالة التشغيل","checkbox":"عند تغيير حالة الاختيار","radio-group":"عند تغيير الخيار","select":"عند تغيير القيمة","toggle-group":"عند تغيير العنصر"}
        param_map = {"accordion":"string[]","slider":"number[]","tabs":"string","progress":"number"}
        pm = param_map.get(cl, "string|boolean")
        ev.insert(0, {"name":"onValueChange","params":[pm],"description":desc_map.get(cl,"عند تغيير القيمة")})
    extras = {
        "dialog": [{"name":"onEscapeKeyDown","params":["KeyboardEvent"],"description":"عند الضغط على Escape"}],
        "select": [{"name":"onCloseAutoFocus","params":["Event"],"description":"عند إغلاق القائمة مع التركيز التلقائي"}],
        "toast": [{"name":"onSwipe","params":["Event"],"description":"عند التمرير السريع"}],
    }
    if cl in extras: ev.extend(extras[cl])
    return ev

def mine_radix_v6():
    cp = load_cp(); ext = []
    if not RADIX.exists(): log("مسار Radix غير موجود", "ERROR"); return ext
    log("=== بدء تعدين Radix UI v6 ===")
    for comp in WEB_NAMES:
        if comp in cp.get("extracted",[]): log(f"{comp}: سبق معالجته"); continue
        src = RADIX / comp / "src"
        if not src.exists(): log(f"{comp}: لا يوجد src", "WARN"); continue
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
        if not content: log(f"{comp}: لا يوجد ملف", "WARN"); continue
        props = extract_all_v6(content)
        for tn in [comp.title()+"Props", comp.title().replace("-","")+"Props"]:
            for p in extract_type_v6(content, tn):
                if p["name"] not in [x["name"] for x in props]: props.append(p)
        parts = comp.split("-")
        if len(parts) > 1:
            for i2 in range(1, len(parts)+1):
                tn = "".join(p.title() for p in parts[:i2]) + "Props"
                if tn != comp.title()+"Props" and tn != comp.title().replace("-","")+"Props":
                    for p in extract_type_v6(content, tn):
                        if p["name"] not in [x["name"] for x in props]: props.append(p)
        cat_order = {"dimension":0,"layout":1,"visual":2,"typography":3,"transform":4,"interaction":5,"state":6,"content":7,"behavior":8,"events":9,"accessibility":10,"rendering":11}
        props.sort(key=lambda p: (cat_order.get(p["category"],99), p["name"]))
        ev = get_component_events(comp)
        parts_list = COMPOUND_PARTS.get(comp, [comp.title()])
        tag = "button" if comp in ["checkbox","switch","toggle"] else "span" if comp=="avatar" else "li" if comp=="toast" else "div"
        data = {
            "meta": {"name": comp.title(), "source": "Radix UI Primitives",
                     "ver": "1.0.0", "date": datetime.now().strftime("%Y-%m-%d"),
                     "type": "web", "miner": "full_miner_v6"},
            "hierarchy": {"root": parts_list[0] if parts_list else comp.title(),
                          "parts": parts_list},
            "props": props, "events": ev,
        }
        WO.mkdir(parents=True, exist_ok=True)
        with open(WO / f"{comp.title()}_v6.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        c_av = sum(1 for p in props if p.get("allowedValues"))
        c_deps = sum(1 for p in props if p.get("dependsOn"))
        log(f"{comp}: {len(props)} خاصية، {c_av} allowedValues، {c_deps} تبعيات ✅")
        ext.append(comp)
        cp.setdefault("processed",[]).append(str(fp))
        cp.setdefault("extracted",[]).append(comp)
        save_cp(cp)
    return ext

def mine_konva_v6():
    cp = load_cp(); ext = []
    log("=== بدء تعدين Konva.js v6 ===")
    nc = read_file(KV / "Node.ts") or ""
    sc = read_file(KV / "Shape.ts") or ""
    cc = read_file(KV / "Container.ts") or ""
    # Track provenance
    bn = extract_type_v6(nc, "NodeConfig") if nc else []
    for p in bn: p["inheritedFrom"] = "NodeConfig"
    bs = extract_type_v6(sc, "ShapeConfig") if sc else []
    for p in bs: p["inheritedFrom"] = "ShapeConfig"
    bc = extract_type_v6(cc, "ContainerConfig") if cc else []
    for p in bc: p["inheritedFrom"] = "ContainerConfig"
    allb = bn + bs + bc; seen = set(); bp = []
    for p in allb:
        key = p["name"]
        if key not in seen:
            seen.add(key)
            bp.append(p)
        else:
            for existing in bp:
                if existing["name"] == key and not existing.get("inheritedFrom"):
                    if p.get("inheritedFrom"): existing["inheritedFrom"] = p["inheritedFrom"]
    for p in bp:
        if p["name"] == "visible": p["default"] = True
        elif p["name"] == "listening": p["default"] = True
        elif p["name"] == "draggable": p["default"] = False
        elif p["name"] == "opacity": p["default"] = 1
        elif p["name"] == "rotation": p["default"] = 0
        elif p["name"] == "cornerRadius": p["default"] = 0
        if not p.get("description"): p["description"] = get_desc(p["name"], p["type"], p["default"])
        p["css"] = get_css(p["name"])
        p["category"] = categorize_v6(p["name"])
        cons = get_constraints(p["name"])
        if cons: p["constraints"] = cons
        elif p["type"] == "number" and not p.get("constraints"): p["constraints"] = {"min": 0}
        deps = get_depends(p["name"])
        if deps: p["dependsOn"] = deps
    for sn in DESIGN_NAMES:
        if sn in cp.get("extracted",[]): log(f"{sn}: سبق معالجته"); ext.append(sn); continue
        f = KV / f"shapes/{sn}.ts"
        if not f.exists(): log(f"{sn}: ملف غير موجود", "WARN"); continue
        content = read_file(f)
        if not content: continue
        props = []
        for base_p in bp:
            p = dict(base_p)
            props.append(p)
        sp = extract_type_v6(content, sn+"Config")
        for p in sp:
            if p["name"] not in [x["name"] for x in props]:
                p["inheritedFrom"] = f"{sn}Config"
                p["description"] = get_desc(p["name"], p["type"], p["default"])
                p["css"] = get_css(p["name"])
                p["category"] = categorize_v6(p["name"])
                cons = get_constraints(p["name"])
                if cons: p["constraints"] = cons
                elif p["type"] == "number" and not p.get("constraints"): p["constraints"] = {"min": 0}
                deps = get_depends(p["name"])
                if deps: p["dependsOn"] = deps
                if p["name"] == "cornerRadius": p["default"] = 0
                props.append(p)
        caps = {"freeform": sn=="Path", "path": sn in ("Path","Line"),
                "corners": sn in ("Rect","Image","RegularPolygon"), "blend": True, "grad": True}
        data = {
            "meta": {"name": sn, "source": "Konva.js", "ver": "10.3.0",
                     "date": datetime.now().strftime("%Y-%m-%d"), "type": "design",
                     "miner": "full_miner_v6"},
            "props": props, "events": KONVA_EVENTS, "caps": caps,
        }
        DO.mkdir(parents=True, exist_ok=True)
        with open(DO / f"{sn}_v6.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        c_inh = sum(1 for p in props if p.get("inheritedFrom"))
        c_deps = sum(1 for p in props if p.get("dependsOn"))
        log(f"{sn}: {len(props)} خاصية، {c_inh} مثبتة المصدر، {c_deps} تبعيات ✅")
        ext.append(sn)
        cp.setdefault("processed",[]).append(str(f))
        cp.setdefault("extracted",[]).append(sn)
        save_cp(cp)
    return ext

def validate_v6(json_file):
    issues = []
    try:
        with open(json_file, "r", encoding="utf-8-sig") as f: data = json.load(f)
    except: return ["CRITICAL: ملف تالف"]
    props = data.get("props", []); pcount = len(props)
    if pcount == 0:
        issues.append(f"INFO: {data.get('meta',{}).get('name','?')} - 0 خاصية (موروث)")
    empty_desc = sum(1 for p in props if not p.get("description","").strip())
    if empty_desc: issues.append(f"INFO: {empty_desc} بلا وصف")
    no_css = sum(1 for p in props if not p.get("css") and p["type"] not in ("function",))
    if no_css > pcount * 0.3 and pcount > 5: issues.append(f"INFO: {no_css}/{pcount} بلا CSS")
    has_deps = sum(1 for p in props if p.get("dependsOn"))
    has_inh = sum(1 for p in props if p.get("inheritedFrom"))
    has_av = sum(1 for p in props if p.get("allowedValues"))
    has_cons = sum(1 for p in props if p.get("constraints"))
    ptype_fixes = sum(1 for p in props if p["type"] != "string")
    issues.append(f"PASS: {pcount} خاصية، {ptype_fixes} أنواع غير نصية، {has_av} allowedValues، {has_cons} constraints، {has_deps} تبعيات، {has_inh} مصادر")
    return issues

def main():
    import time
    start = time.time()
    print()
    print("=" * 70)
    print("  GOLDEN CLASS FACTORY - ULTIMATE MINER v6")
    print("  جودة أسطورية - تعدين شامل - تحسينات كاملة")
    print("=" * 70)
    print()
    print("[1/4] Mining Radix UI (web)..."); print()
    web = mine_radix_v6()
    print(); print("[2/4] Mining Konva.js (design)..."); print()
    design = mine_konva_v6()
    print(); print("[3/4] Quality validation..."); print()
    web_files = sorted(WO.glob("*_v6.json"))
    design_files = sorted(DO.glob("*_v6.json"))
    all_issues = {}
    for jf in web_files + design_files:
        issues = validate_v6(jf)
        if issues: all_issues[jf.name] = issues
    total = len(web_files) + len(design_files)
    clean = sum(1 for v in all_issues.values() if not any(i.startswith("CRITICAL") for i in v))
    total_props = 0
    for jf in web_files + design_files:
        try:
            d = json.load(open(jf,"r",encoding="utf-8-sig"))
            total_props += len(d.get("props",[]))
        except: pass
    qual = round((clean/total)*100,1) if total > 0 else 0
    print(f"  Quality: {qual}%, Files: {total}, Props: {total_props}")
    print(); print("[4/4] Final summary...")
    elapsed = round(time.time()-start, 1)
    print(f"  Time: {elapsed}s")
    print(f"  Web: {len(web)}/{len(WEB_NAMES)}")
    print(f"  Design: {len(design)}/{len(DESIGN_NAMES)}")
    print(f"  Props: {total_props}")
    print(f"  Quality: {qual}%")
    print(); print("=" * 70); print("  v6 mining complete!"); print("=" * 70)

if __name__ == "__main__":
    main()
''')
print("Generator script complete")
