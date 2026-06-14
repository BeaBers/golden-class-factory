#!/usr/bin/env python3
"""Golden Class Factory v6 - Ultimate Miner with 9 Improvements"""
import os, re, json, sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

# ============================================================
# Paths
# ============================================================
ROOT = Path("C:/Users/Administrator/Desktop/WebProject")
RADIX = ROOT / "01-mines" / "web-mine" / "radix-ui" / "packages" / "react"
KV = ROOT / "01-mines" / "design-mine" / "konva" / "src"
WO = ROOT / "03-gold-boxes" / "web-props"
DO = ROOT / "03-gold-boxes" / "design-props"
CP_PATH = ROOT / "mining_checkpoint.json"

WEB_NAMES = [
    "accordion","alert-dialog","avatar","checkbox","collapsible",
    "dialog","hover-card","popover","progress","radio-group",
    "select","slider","switch","tabs","toast","toggle",
    "toggle-group","tooltip",
]
DESIGN_NAMES = [
    "Arc","Arrow","Circle","Ellipse","Image","Label","Line",
    "Path","Rect","RegularPolygon","Ring","Star","Tag","Text","TextPath",
]

# ============================================================
# Utilities
# ============================================================
def log(msg, level="INFO"):
    print(f"  [{level}] {msg}")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            return f.read()
    except: return ""

def load_cp():
    if CP_PATH.exists():
        try:
            with open(CP_PATH, "r", encoding="utf-8-sig") as f:
                return json.load(f)
        except: pass
    return {"extracted": [], "processed": []}

def save_cp(cp):
    with open(CP_PATH, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2)

# ============================================================
# CSS_MAP (180+ properties)
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
    "children": None, "label": None,
    "max": "max (HTML attribute)", "min": "min (HTML attribute)", "step": "step (HTML attribute)",
    "orientation": "flex-direction (logical)",
    "altText": "alt (HTML attribute)",
    "pressed": None, "defaultPressed": None, "present": None,
    "modal": None, "loop": None, "collapsible": None,
    "rovingFocus": None, "trapFocus": None, "inverted": None,
    "hotkey": None, "activationMode": None, "focusVisible": None,
    "disableHoverableContent": None, "getValueLabel": None,
    "announcerContainer": None,
    "duration": None, "delayDuration": None, "delayMs": None,
    "openDelay": None, "closeDelay": None, "skipDelayDuration": None,
    "swipeDirection": None, "swipeThreshold": None,
    "minStepsBetweenThumbs": None,
    "onFocusFromOutsideViewport": None, "onFocusOutside": None,
    "onInteractOutside": None, "onOpenAutoFocus": None,
    "onPressedChange": None, "onValueCommit": None,
    "onPause": None, "onResume": None,
    "onSwipeStart": None, "onSwipeMove": None, "onSwipeEnd": None, "onSwipeCancel": None,

}
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
DESC_TEMPLATES = {
    "x": "Ahorizontal position (X) of the element relative to parent",
    "y": "Vertical position (Y) of the element relative to parent",
    "width": "The element width", "height": "The element height",
    "fill": "Fill color of the element", "stroke": "Outline stroke color",
    "strokeWidth": "Outline stroke width",
    "opacity": "Element opacity (0=transparent, 1=opaque)",
    "visible": "Toggle visibility of the element",
    "rotation": "Rotation angle in degrees (-360 to 360)",
    "rotationDeg": "Rotation angle in degrees (0-360)",
    "cornerRadius": "Radius of border corners",
    "shadowColor": "Color of the box shadow behind the element",
    "shadowBlur": "Blur radius of the shadow",
    "shadowOffsetX": "Horizontal shadow offset (positive=right)",
    "shadowOffsetY": "Vertical shadow offset (positive=down)",
    "shadowOpacity": "Shadow opacity (0=transparent, 1=opaque)",
    "shadowOffset": "Shadow offset (X,Y)",
    "shadowEnabled": "Enable/disable shadow on element",
    "shadowForStrokeEnabled": "Show shadow on stroke area",
    "scaleX": "Horizontal scale factor (1=normal)",
    "scaleY": "Vertical scale factor (1=normal)",
    "scale": "Uniform scale factor",
    "skewX": "Horizontal skew angle", "skewY": "Vertical skew angle",
    "dash": "Pattern of dashes: [dash_length, gap_length]",
    "dashOffset": "Offset position of dash pattern",
    "lineCap": "Line end style: butt (flat), round, square",
    "lineJoin": "Corner join style: miter (pointed), round, bevel",
    "miterLimit": "Maximum miter length for miter join",
    "draggable": "Allow element to be dragged",
    "dragDistance": "Minimum distance before drag starts",
    "dragBoundFunc": "Function to limit drag boundaries",
    "preventDefault": "Prevent default browser behavior",
    "disabled": "Disable interaction with element",
    "fontSize": "Font size in pixels",
    "fontFamily": "Font family name",
    "fontWeight": "Font weight (400=normal, 700=bold)",
    "fontStyle": "Font style (normal, italic, oblique)",
    "fontVariant": "Font variant (normal, small-caps)",
    "textAlign": "Text horizontal alignment",
    "verticalAlign": "Text vertical alignment",
    "lineHeight": "Line height (multiplier relative to font size)",
    "letterSpacing": "Space between characters",
    "wordSpacing": "Space between words",
    "color": "Text color", "textColor": "Text color",
    "textDecoration": "Text decoration (underline, line-through)",
    "textTransform": "Text case transform (uppercase, lowercase)",
    "whiteSpace": "How whitespace inside element is handled",
    "overflow": "How overflowing content is handled",
    "textOverflow": "How text overflow is indicated (ellipsis=...)",
    "wrap": "Text wrapping behavior",
    "ellipsis": "Show ... when text overflows",
    "direction": "Text direction (ltr=left-right, rtl=right-left)",
    "align": "Text alignment", "underlineOffset": "Text underline position offset",
    "padding": "Internal padding space",
    "margin": "External margin space",
    "gap": "Gap between flex/grid child elements",
    "flexDirection": "Flex direction: row (horizontal), column (vertical)",
    "flexWrap": "Whether flex items wrap to next line",
    "justifyContent": "Main axis alignment of flex items",
    "alignItems": "Cross axis alignment of flex items",
    "borderWidth": "Border stroke width",
    "borderColor": "Border stroke color",
    "borderStyle": "Border stroke style (solid, dashed)",
    "borderRadius": "Border corner radius",
    "variant": "Component variant: solid, outline, ghost, link",
    "size": "Component size: sm (small), md (medium), lg (large)",
    "colorScheme": "Component color scheme",
    "label": "Accessible label for the component",
    "placeholder": "Placeholder text when empty",
    "id": "Element unique identifier (HTML id)",
    "className": "CSS class name string",
    "name": "Element name (used in forms)",
    "value": "Current value of the element",
    "defaultValue": "Default value initial",
    "checked": "Checked state (true=checked)",
    "defaultChecked": "Default checked state initial",
    "required": "Field is required", "readOnly": "Field is read-only",
    "autoFocus": "Auto-focus on mount",
    "tabIndex": "Tab key navigation order",
    "asChild": "Render as child element instead of default",
    "as": "Render as specified HTML element",
    "forceMount": "Force mount in DOM regardless of state",
    "defaultOpen": "Default open state initial", "open": "Open/expanded state",
    "listening": "Enable event listeners for element",
    "hitStrokeWidth": "Hit detection width of stroke",
    "strokeScaleEnabled": "Scale stroke when element scales",
    "strokeHitEnabled": "Enable hit detection on stroke",
    "fillEnabled": "Enable fill rendering",
    "fillPriority": "Fill rendering priority (color/gradient/pattern)",
    "fillRule": "Fill rule for overlapping paths",
    "fillPatternImage": "Image used for fill pattern",
    "fillPatternX": "Pattern horizontal offset",
    "fillPatternY": "Pattern vertical offset",
    "fillPatternRepeat": "Pattern repetition mode",
    "fillLinearGradientColorStops": "Linear gradient color stop values",
    "fillRadialGradientColorStops": "Radial gradient color stop values",
    "globalCompositeOperation": "Global compositing blend mode",
    "filters": "Canvas filters (blur, brightness...)",
    "sceneFunc": "Custom scene rendering function",
    "hitFunc": "Custom hit detection function",
    "clipFunc": "Custom clipping function",
    "clipX": "X position of clip region", "clipY": "Y position of clip region",
    "clipWidth": "Width of clip region", "clipHeight": "Height of clip region",
    "clearBeforeDraw": "Clear canvas before redraw",
    "perfectDrawEnabled": "Enable high-quality rendering",
    "children": "Child elements contained within",
    "container": "Portal container element",
    "nonce": "CSP nonce hash value", "form": "Associated HTML form",
    "textValue": "Alternative text value for accessibility",
    "autoComplete": "Browser autocomplete suggestions",
    "dir": "Writing direction (rtl=right-left, ltr=left-right)",
}
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
    {"name":"click","params":["MouseEvent"],"description":"Fires when shape is clicked"},
    {"name":"dblclick","params":["MouseEvent"],"description":"Fires on double click"},
    {"name":"mousedown","params":["MouseEvent"],"description":"Fires on mouse button press"},
    {"name":"mouseup","params":["MouseEvent"],"description":"Fires on mouse button release"},
    {"name":"mouseenter","params":["MouseEvent"],"description":"Fires when mouse enters shape area"},
    {"name":"mouseleave","params":["MouseEvent"],"description":"Fires when mouse leaves shape area"},
    {"name":"touchstart","params":["TouchEvent"],"description":"Fires on touch start"},
    {"name":"touchend","params":["TouchEvent"],"description":"Fires on touch end"},
    {"name":"dragstart","params":["DragEvent"],"description":"Fires when drag starts"},
    {"name":"dragmove","params":["DragEvent"],"description":"Fires during dragging"},
    {"name":"dragend","params":["DragEvent"],"description":"Fires when drag ends"},
    {"name":"transform","params":["Event"],"description":"Fires during transform"},
    {"name":"mousewheel","params":["WheelEvent"],"description":"Fires on mouse wheel scroll"},
    {"name":"contextmenu","params":["MouseEvent"],"description":"Fires on right-click"},
    {"name":"dbltap","params":["TouchEvent"],"description":"Fires on double tap (touch)"},
    {"name":"tap","params":["TouchEvent"],"description":"Fires on single tap (touch)"},
]

RADIX_EVENTS_BASE = [
    {"name":"onClick","params":["React.MouseEvent"],"description":"Fires when the component is clicked"},
    {"name":"onFocus","params":["React.FocusEvent"],"description":"Fires when the component gains focus"},
    {"name":"onBlur","params":["React.FocusEvent"],"description":"Fires when the component loses focus"},
]

def get_component_events(cname):
    cl = cname.lower()
    ev = list(RADIX_EVENTS_BASE)
    open_close = ["dialog","popover","tooltip","hover-card","alert-dialog","collapsible"]
    value_change = ["select","radio-group","toggle","switch","checkbox","slider","progress","tabs","accordion","toggle-group"]
    if cl in open_close:
        ev.insert(0, {"name":"onOpenChange","params":["boolean"],"description":"Fires when open/closed state changes"})
    if cl in value_change:
        desc_map = {"accordion":"Fires when expanded item changes","slider":"Fires when slider value changes","tabs":"Fires when active tab changes","progress":"Fires when progress value changes","toggle":"Fires when toggle state changes","switch":"Fires when switch state changes","checkbox":"Fires when check state changes","radio-group":"Fires when selection changes","select":"Fires when value changes","toggle-group":"Fires when active item changes"}
        param_map = {"accordion":"string[]","slider":"number[]","tabs":"string","progress":"number"}
        pm = param_map.get(cl, "string|boolean")
        ev.insert(0, {"name":"onValueChange","params":[pm],"description":desc_map.get(cl,"Fires when value changes")})
    extras = {
        "dialog": [{"name":"onEscapeKeyDown","params":["KeyboardEvent"],"description":"Fires when Escape key is pressed"}],
        "alert-dialog": [{"name":"onEscapeKeyDown","params":["KeyboardEvent"],"description":"Fires when Escape key is pressed"}],
        "select": [{"name":"onCloseAutoFocus","params":["Event"],"description":"Fires after close with auto-focus management"}],
        "toast": [{"name":"onSwipe","params":["Event"],"description":"Fires when the toast is swiped"}],
    }
    if cl in extras: ev.extend(extras[cl])
    return ev
# ============================================================
# Core Type Detection & Categorization
# ============================================================
def map_type_v6(t, name=""):
    t = t.strip()
    if t == "boolean": return "boolean", "toggle", None
    if t == "string": return "string", "text_input", None
    if t == "number": return "number", "slider", None
    stripped = t.replace(" ", "")
    if any(x in stripped for x in ["=>", "):", "Function"]):
        return "function", "code_input", None
    if t.startswith("(") and ("=>" in t or "):" in t):
        return "function", "code_input", None
    if "'" in t and "|" in t:
        vals = [v.strip().strip("'") for v in t.split("|") if v.strip()]
        return "enum", "select", vals
    if "[]" in t or t.startswith("Array"):
        return "array", "text_input", None
    if any(x in t for x in ["React.ReactNode", "ReactNode", "React.Element"]):
        return "component", "component_picker", None
    if any(x in t for x in ["MouseEvent", "KeyboardEvent", "FocusEvent", "TouchEvent", "WheelEvent", "DragEvent"]):
        return "function", "code_input", None
    return "string", "text_input", None

def categorize_v6(name):
    n = name.lower()
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
            d += f" (default: {default_val})"
        return d
    t_map = {"boolean": " (toggle)", "number": " (numeric)", "string": " (text)",
             "function": " (callback)", "array": " (array)", "enum": " (select)"}
    return f"Property {name}" + t_map.get(ptype, "")

def get_depends(name):
    return DEPENDENCY_MAP.get(name, None)
# ============================================================
# TS Parsing
# ============================================================
def parse_ts_v6(lines, source_name=""):
    props = []
    if isinstance(lines, str): lines = lines.split("\n")
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
        for p in parse_ts_v6(body.split("\n"), m.group(1)):
            if p["name"] not in [x["name"] for x in allp]:
                allp.append(p)
    return allp

def extract_type_v6(content, tname):
    for pat in [
        r"interface\s+" + re.escape(tname) + r"(?:<[^>]*>)?(?:\s+extends\s+[^{]+)?\s*\{",
        r"type\s+" + re.escape(tname) + r"(?:<[^>]*>)?\s*=\s*(?:[^{]*?\&\s*)?\{",
    ]:
        m = re.search(pat, content)
        if m:
            si = m.end() - 1
            ei = extract_block(content, si)
            return parse_ts_v6(content[si+1:ei].split("\n"), tname)
    return []
# ============================================================
# Radix UI Mining
# ============================================================
def mine_radix_v6():
    cp = load_cp(); ext = []
    if not RADIX.exists(): log("Radix path not found", "ERROR"); return ext
    log("=== Mining Radix UI v6 ===")
    for comp in WEB_NAMES:
        if comp in cp.get("extracted",[]): log(f"{comp}: already processed"); continue
        src = RADIX / comp / "src"
        if not src.exists(): log(f"{comp}: no src dir", "WARN"); continue
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
        if not content: log(f"{comp}: no readable file", "WARN"); continue
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
        cf = get_css_formats(props)
        data = {
            "meta": {"name": comp.title(), "source": "Radix UI Primitives",
                     "ver": "1.0.0", "date": datetime.now().strftime("%Y-%m-%d"),
                     "type": "web", "miner": "full_miner_v6"},
            "hierarchy": {"root": parts_list[0] if parts_list else comp.title(),
                          "parts": parts_list},
            "props": props, "events": ev,
        }
        if cf: data["cssFormat"] = cf
        WO.mkdir(parents=True, exist_ok=True)
        with open(WO / f"{comp.title()}_v6.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        c_av = sum(1 for p in props if p.get("allowedValues"))
        c_deps = sum(1 for p in props if p.get("dependsOn"))
        c_inh = sum(1 for p in props if p.get("inheritedFrom"))
        log(f"{comp}: {len(props)} props, {c_av} allowedValues, {c_deps} deps, {c_inh} inherited")
        ext.append(comp)
        cp.setdefault("processed",[]).append(str(fp))
        cp.setdefault("extracted",[]).append(comp)
        save_cp(cp)
    return ext

# ============================================================
# Konva.js Mining
# ============================================================
def mine_konva_v6():
    cp = load_cp(); ext = []
    log("=== Mining Konva.js v6 ===")
    nc = read_file(KV / "Node.ts") or ""
    sc = read_file(KV / "Shape.ts") or ""
    cc = read_file(KV / "Container.ts") or ""
    # Extract base configs with provenance
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
        if sn in cp.get("extracted",[]): log(f"{sn}: already processed"); ext.append(sn); continue
        f = KV / f"shapes/{sn}.ts"
        if not f.exists(): log(f"{sn}: file not found", "WARN"); continue
        content = read_file(f)
        if not content: continue
        props = [dict(base_p) for base_p in bp]
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
        cf = get_css_formats(props)
        data = {
            "meta": {"name": sn, "source": "Konva.js", "ver": "10.3.0",
                     "date": datetime.now().strftime("%Y-%m-%d"), "type": "design",
                     "miner": "full_miner_v6"},
            "props": props, "events": KONVA_EVENTS, "caps": caps,
        }
        if cf: data["cssFormat"] = cf
        DO.mkdir(parents=True, exist_ok=True)
        with open(DO / f"{sn}_v6.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        c_inh = sum(1 for p in props if p.get("inheritedFrom"))
        c_deps = sum(1 for p in props if p.get("dependsOn"))
        log(f"{sn}: {len(props)} props, {c_inh} provenance, {c_deps} deps")
        ext.append(sn)
        cp.setdefault("processed",[]).append(str(f))
        cp.setdefault("extracted",[]).append(sn)
        save_cp(cp)
    return ext
# ============================================================
# Quality Validation
# ============================================================

def get_css_formats(props):
    pnames = {p["name"] for p in props}
    formats = {}
    if {"shadowColor","shadowBlur","shadowOffsetX","shadowOffsetY"}.issubset(pnames):
        formats["shadow"] = "box-shadow: {shadowOffsetX}px {shadowOffsetY}px {shadowBlur}px {shadowColor}"
    if {"borderWidth","borderStyle","borderColor"}.issubset(pnames):
        formats["border"] = "border: {borderWidth}px {borderStyle} {borderColor}"
    if {"outlineWidth","outlineStyle","outlineColor"}.issubset(pnames):
        formats["outline"] = "outline: {outlineWidth}px {outlineStyle} {outlineColor}"
    if "dash" in pnames:
        formats["dash"] = "stroke-dasharray: {dash}"
    if {"x","y","rotation","scaleX","scaleY"}.issubset(pnames):
        formats["transform"] = "transform: translate({x}px,{y}px) rotate({rotation}deg) scale({scaleX},{scaleY})"
    if {"clipY","clipWidth","clipHeight","clipX"}.issubset(pnames):
        formats["clipPath"] = "clip-path: inset({clipY}px {clipWidth}px {clipHeight}px {clipX}px)"
    return formats if formats else None

def validate_v6(json_file):
    issues = []
    try:
        with open(json_file, "r", encoding="utf-8-sig") as f: data = json.load(f)
    except: return ["CRITICAL: corrupt file"]
    meta = data.get("meta", {})
    props = data.get("props", []); pcount = len(props)
    if pcount == 0:
        issues.append(f"INFO: {meta.get('name','?')} - 0 props (inherited)")
    empty_desc = sum(1 for p in props if not p.get("description","").strip())
    if empty_desc: issues.append(f"INFO: {empty_desc} without description")
    no_css = sum(1 for p in props if p.get("css") is None and p["type"] not in ("function",))
    if no_css > pcount * 0.5 and pcount > 3: issues.append(f"INFO: {no_css}/{pcount} no CSS (framework-specific)")
    has_deps = sum(1 for p in props if p.get("dependsOn"))
    has_inh = sum(1 for p in props if p.get("inheritedFrom"))
    has_av = sum(1 for p in props if p.get("allowedValues"))
    has_cons = sum(1 for p in props if p.get("constraints"))
    type_fixes = sum(1 for p in props if p["type"] != "string")
    wrong_type = sum(1 for p in props if p["type"] == "string" and p.get("allowedValues"))
    if wrong_type > 2: issues.append(f"WARN: {wrong_type} props should be enum (have allowedValues)")
    issues.append(f"PASS: {pcount} props, {type_fixes} typed, {has_av} allowedValues, {has_cons} constraints, {has_deps} deps, {has_inh} provenance")
    return issues

# ============================================================
# Main
# ============================================================
def main():
    import time
    start = time.time()
    print()
    print("=" * 70)
    print("  GOLDEN CLASS FACTORY - ULTIMATE MINER v6")
    print("  9 Improvements: types, enums, constraints, CSS, descs, cats, deps, formats, provenance")
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

