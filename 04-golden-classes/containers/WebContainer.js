class WebContainer extends BaseComponent {
  constructor(options = {}) {
    super(options);
    this.type = 'WebContainer';

    this.loadSchema({
      meta: { name: 'WebContainer', source: 'Golden Class Factory', ver: '1.0.0', type: 'container' },
      props: [
        { name: 'width', type: 'number', default: 800, uiControl: 'slider', category: 'dimension', css: 'width' },
        { name: 'height', type: 'number', default: 600, uiControl: 'slider', category: 'dimension', css: 'height' },
        { name: 'x', type: 'number', default: 0, uiControl: 'slider', category: 'dimension', css: 'left' },
        { name: 'y', type: 'number', default: 0, uiControl: 'slider', category: 'dimension', css: 'top' },
        { name: 'fill', type: 'string', default: '#ffffff', uiControl: 'color', category: 'visual', css: 'background-color' },
        { name: 'opacity', type: 'number', default: 1, uiControl: 'slider', category: 'visual', css: 'opacity', constraints: { min: 0, max: 1 } },
        { name: 'cornerRadius', type: 'number', default: 0, uiControl: 'slider', category: 'visual', css: 'border-radius', constraints: { min: 0 } },
        { name: 'borderWidth', type: 'number', default: 0, uiControl: 'slider', category: 'visual', css: 'border-width', constraints: { min: 0 } },
        { name: 'borderColor', type: 'string', default: '#000000', uiControl: 'color', category: 'visual', css: 'border-color' },
        { name: 'shadowColor', type: 'string', default: null, uiControl: 'color', category: 'visual', css: 'box-shadow-color' },
        { name: 'shadowBlur', type: 'number', default: 0, uiControl: 'slider', category: 'visual', css: 'box-shadow-blur-radius', constraints: { min: 0 } },
        { name: 'shadowOffsetX', type: 'number', default: 0, uiControl: 'slider', category: 'visual' },
        { name: 'shadowOffsetY', type: 'number', default: 0, uiControl: 'slider', category: 'visual' },
        { name: 'gap', type: 'number', default: 8, uiControl: 'slider', category: 'layout', css: 'gap' },
        { name: 'flexDirection', type: 'string', default: 'row', allowedValues: ['row', 'column'], uiControl: 'select', category: 'layout', css: 'flex-direction' },
        { name: 'justifyContent', type: 'string', default: 'flex-start', allowedValues: ['flex-start', 'center', 'flex-end', 'space-between', 'space-around'], uiControl: 'select', category: 'layout', css: 'justify-content' },
        { name: 'alignItems', type: 'string', default: 'flex-start', allowedValues: ['flex-start', 'center', 'flex-end', 'stretch'], uiControl: 'select', category: 'layout', css: 'align-items' },
        { name: 'flexWrap', type: 'string', default: 'nowrap', allowedValues: ['nowrap', 'wrap'], uiControl: 'select', category: 'layout', css: 'flex-wrap' },
        { name: 'padding', type: 'number', default: 0, uiControl: 'slider', category: 'layout', css: 'padding', constraints: { min: 0 } },
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
        { name: 'dragstart', params: ['DragEvent'] },
        { name: 'dragmove', params: ['DragEvent'] },
        { name: 'dragend', params: ['DragEvent'] }
      ],
      caps: { freeform: false, path: false, corners: true, blend: true, grad: false }
    });

    this.setRenderer((self, canvas, parentNode) => {
      if (typeof Leafer !== 'undefined') {
        const rect = new Leafer.Rect({
          x: self.props.x || 0,
          y: self.props.y || 0,
          width: self.props.width || 800,
          height: self.props.height || 600,
          fill: self.props.fill || '#ffffff',
          opacity: self.props.opacity ?? 1,
          cornerRadius: self.props.cornerRadius || 0,
          stroke: self.props.borderColor,
          strokeWidth: self.props.borderWidth || 0,
          shadowColor: self.props.shadowColor,
          shadowBlur: self.props.shadowBlur || 0,
          shadowOffsetX: self.props.shadowOffsetX || 0,
          shadowOffsetY: self.props.shadowOffsetY || 0,
          draggable: self.props.draggable || false,
          visible: self.props.visible ?? true
        });
        if (parentNode) {
          parentNode.add(rect);
        } else if (canvas && canvas.add) {
          canvas.add(rect);
        }
        return rect;
      }
      return null;
    });

    this.setExporter({
      toAST: (self) => {
        const style = [];
        if (self.props.width && self.props.width !== 800) style.push(\width:\px\);
        if (self.props.height && self.props.height !== 600) style.push(\height:\px\);
        if (self.props.fill && self.props.fill !== '#ffffff') style.push(\ackground:\\);
        if (self.props.opacity !== undefined && self.props.opacity !== 1) style.push(\opacity:\\);
        if (self.props.cornerRadius) style.push(\order-radius:\px\);
        if (self.props.borderWidth) style.push(\order:\px solid \\);
        if (self.props.padding) style.push(\padding:\px\);
        style.push('display:flex');
        style.push(\lex-direction:\\);
        style.push(\justify-content:\\);
        style.push(\lign-items:\\);
        if (self.props.gap !== 8) style.push(\gap:\px\);
        if (self.props.flexWrap !== 'nowrap') style.push(\lex-wrap:\\);
        if (self.props.shadowBlur) {
          style.push(\ox-shadow:\px \px \px \\);
        }
        if (self.props.x) style.push(\left:\px\);
        if (self.props.y) style.push(\	op:\px\);

        const attrs = { class: \gc-container \\.trim() };
        if (self.props.id) attrs.id = self.props.id;
        if (style.length) attrs.style = style.join(';');

        return {
          tagName: 'div',
          attributes: attrs,
          children: self.children.map(c => c.exportToAST())
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
  module.exports = { WebContainer };
}
