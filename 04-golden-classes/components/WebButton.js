class WebButton extends BaseComponent {
  constructor(options = {}) {
    super(options);
    this.type = 'WebButton';

    this.loadSchema({
      meta: { name: 'WebButton', source: 'Radix UI + Golden Class Factory', ver: '1.0.0', type: 'component' },
      props: [
        { name: 'x', type: 'number', default: 0, uiControl: 'slider', category: 'dimension', css: 'left' },
        { name: 'y', type: 'number', default: 0, uiControl: 'slider', category: 'dimension', css: 'top' },
        { name: 'width', type: 'number', default: 120, uiControl: 'slider', category: 'dimension', css: 'width' },
        { name: 'height', type: 'number', default: 40, uiControl: 'slider', category: 'dimension', css: 'height' },
        { name: 'label', type: 'string', default: 'Button', uiControl: 'text_input', category: 'content' },
        { name: 'variant', type: 'string', default: 'solid', allowedValues: ['solid', 'outline', 'ghost', 'link'], uiControl: 'select', category: 'visual' },
        { name: 'colorScheme', type: 'string', default: 'blue', allowedValues: ['blue', 'red', 'green', 'gray', 'black'], uiControl: 'select', category: 'visual', css: 'background-color' },
        { name: 'size', type: 'string', default: 'md', allowedValues: ['sm', 'md', 'lg'], uiControl: 'select', category: 'visual' },
        { name: 'fill', type: 'string', default: '#3b82f6', uiControl: 'color', category: 'visual', css: 'background-color' },
        { name: 'textColor', type: 'string', default: '#ffffff', uiControl: 'color', category: 'visual', css: 'color' },
        { name: 'fontSize', type: 'number', default: 14, uiControl: 'slider', category: 'typography', css: 'font-size', constraints: { min: 8, max: 72 } },
        { name: 'fontWeight', type: 'string', default: '600', allowedValues: ['400', '500', '600', '700'], uiControl: 'select', category: 'typography', css: 'font-weight' },
        { name: 'cornerRadius', type: 'number', default: 6, uiControl: 'slider', category: 'visual', css: 'border-radius', constraints: { min: 0 } },
        { name: 'borderWidth', type: 'number', default: 0, uiControl: 'slider', category: 'visual', css: 'border-width', constraints: { min: 0 } },
        { name: 'borderColor', type: 'string', default: null, uiControl: 'color', category: 'visual', css: 'border-color' },
        { name: 'opacity', type: 'number', default: 1, uiControl: 'slider', category: 'visual', css: 'opacity', constraints: { min: 0, max: 1 } },
        { name: 'disabled', type: 'boolean', default: false, uiControl: 'toggle', category: 'state' },
        { name: 'visible', type: 'boolean', default: true, uiControl: 'toggle', category: 'visual', css: 'visibility' },
        { name: 'draggable', type: 'boolean', default: false, uiControl: 'toggle', category: 'interaction' },
        { name: 'id', type: 'string', default: null, uiControl: 'text_input', category: 'content', css: 'id (HTML attribute)' },
        { name: 'className', type: 'string', default: null, uiControl: 'text_input', category: 'content', css: 'class' }
      ],
      events: [
        { name: 'click', params: ['MouseEvent'] },
        { name: 'dblclick', params: ['MouseEvent'] },
        { name: 'mousedown', params: ['MouseEvent'] },
        { name: 'mouseup', params: ['MouseEvent'] },
        { name: 'mouseenter', params: ['MouseEvent'] },
        { name: 'mouseleave', params: ['MouseEvent'] },
        { name: 'focus', params: ['FocusEvent'] },
        { name: 'blur', params: ['FocusEvent'] },
        { name: 'keydown', params: ['KeyboardEvent'] }
      ],
      caps: { freeform: false, path: false, corners: true, blend: false, grad: false }
    });

    this.setRenderer((self, canvas, parentNode) => {
      if (typeof Leafer !== 'undefined') {
        const sizeMap = { sm: { w: 80, h: 32, fs: 12 }, md: { w: 120, h: 40, fs: 14 }, lg: { w: 160, h: 48, fs: 16 } };
        const sz = sizeMap[self.props.size || 'md'];
        const w = self.props.width ?? sz.w;
        const h = self.props.height ?? sz.h;
        const fill = self.props.disabled ? '#9ca3af' : (self.props.fill || '#3b82f6');

        const group = new Leafer.Group({ x: self.props.x || 0, y: self.props.y || 0, draggable: self.props.draggable });

        const bg = new Leafer.Rect({
          width: w, height: h,
          fill, cornerRadius: self.props.cornerRadius ?? 6,
          stroke: self.props.borderColor || (self.props.variant === 'outline' ? fill : undefined),
          strokeWidth: self.props.borderWidth || (self.props.variant === 'outline' ? 2 : 0),
          opacity: self.props.opacity ?? 1,
          visible: self.props.visible ?? true
        });
        group.add(bg);

        const text = new Leafer.Text({
          text: self.props.label || 'Button',
          fontSize: self.props.fontSize ?? sz.fs,
          fill: self.props.textColor || '#ffffff',
          fontWeight: self.props.fontWeight || '600',
          textAlign: 'center',
          verticalAlign: 'middle',
          x: w / 2, y: h / 2
        });
        group.add(text);

        if (parentNode) {
          parentNode.add(group);
        } else if (canvas && canvas.add) {
          canvas.add(group);
        }

        self._leaferNode = group;
        self._leaferBg = bg;
        self._leaferText = text;
        return group;
      }
      return null;
    });

    this.setExporter({
      toAST: (self) => {
        const sizeMap = { sm: { w: 80, h: 32, fs: 12, px: 8, py: 4 }, md: { w: 120, h: 40, fs: 14, px: 12, py: 8 }, lg: { w: 160, h: 48, fs: 16, px: 16, py: 12 } };
        const sz = sizeMap[self.props.size || 'md'];
        const style = [];
        const fill = self.props.disabled ? '#9ca3af' : (self.props.fill || '#3b82f6');
        const txtColor = self.props.disabled ? '#d1d5db' : (self.props.textColor || '#ffffff');

        if (self.props.width) style.push(\width:\px\);
        if (self.props.height) style.push(\height:\px\);
        style.push('display:inline-flex');
        style.push('align-items:center');
        style.push('justify-content:center');
        style.push(\padding:\px \px\);
        style.push(\ackground:\\);
        style.push(\color:\\);
        style.push(\ont-size:\px\);
        style.push(\ont-weight:\\);
        style.push(\order-radius:\px\);
        style.push(\order:\px solid \\);
        style.push(\cursor:\\);
        style.push(\opacity:\\);
        style.push('text-decoration:none');

        if (self.props.x) style.push(\left:\px\);
        if (self.props.y) style.push(\	op:\px\);

        const attrs = { class: \gc-button \\.trim() };
        if (self.props.id) attrs.id = self.props.id;
        if (self.props.disabled) attrs.disabled = 'disabled';
        attrs.style = style.join(';');

        return {
          tagName: 'button',
          attributes: attrs,
          children: [self.props.label || 'Button']
        };
      }
    });

    this.setLogicHandler((self, canvas) => {
      if (self._leaferNode && self._events) {
        Object.keys(self._events).forEach(eventName => {
          if (self._leaferNode.on) {
            self._leaferNode.on(eventName, (e) => self.emit(eventName, e));
          }
        });
      }
    });
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { WebButton };
}
