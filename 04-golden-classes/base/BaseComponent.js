class BaseComponent {
  constructor(options = {}) {
    this.id = options.id || gc_\_\;
    this.type = options.type || 'BaseComponent';
    this.parentId = options.parentId || null;
    this.children = [];
    this.props = {};
    this._events = {};
    this._uiSchema = null;
    this._canvasRenderer = null;
    this._webExporter = null;
    this._logicHandler = null;
    this._leaferNode = null;
  }

  loadSchema(schema) {
    this._uiSchema = schema;
    if (schema && schema.props) {
      schema.props.forEach(prop => {
        if (prop.default !== null && prop.default !== undefined) {
          this.props[prop.name] = prop.default;
        }
      });
    }
    return this;
  }

  setRenderer(rendererFn) {
    this._canvasRenderer = rendererFn;
    return this;
  }

  setExporter(exporterObj) {
    this._webExporter = exporterObj;
    return this;
  }

  setLogicHandler(handlerFn) {
    this._logicHandler = handlerFn;
    return this;
  }

  setProp(name, value) {
    this.props[name] = value;
    return this;
  }

  getProp(name) {
    return this.props[name];
  }

  on(event, handler) {
    if (!this._events[event]) this._events[event] = [];
    this._events[event].push(handler);
    return this;
  }

  off(event, handler) {
    if (!this._events[event]) return;
    this._events[event] = this._events[event].filter(h => h !== handler);
    return this;
  }

  emit(event, data) {
    if (!this._events[event]) return;
    this._events[event].forEach(h => h({ target: this, type: event, data }));
    return this;
  }

  addChild(child) {
    child.parentId = this.id;
    this.children.push(child);
    return this;
  }

  removeChild(childId) {
    this.children = this.children.filter(c => c.id !== childId);
    return this;
  }

  getSchema() {
    return this._uiSchema;
  }

  render(canvas, parentNode) {
    if (this._canvasRenderer) {
      this._leaferNode = this._canvasRenderer(this, canvas, parentNode);
    }
    this.children.forEach(child => child.render(canvas, this._leaferNode));
    return this._leaferNode;
  }

  exportToAST() {
    if (this._webExporter && this._webExporter.toAST) {
      return this._webExporter.toAST(this);
    }
    return { tagName: 'div', attributes: {}, children: [] };
  }

  exportToTailwind() {
    const ast = this.exportToAST();
    return this._astToHtml(ast);
  }

  _astToHtml(ast) {
    if (!ast) return '';
    if (typeof ast === 'string') return ast;
    const attrs = Object.entries(ast.attributes || {})
      .map(([k, v]) => \\="\"\).join(' ');
    const children = (ast.children || [])
      .map(c => this._astToHtml(c)).join('\n');
    return \<\\>\</\>\;
  }

  attachLogic(canvas) {
    if (this._logicHandler) {
      this._logicHandler(this, canvas);
    }
    this.children.forEach(child => child.attachLogic(canvas));
  }

  toJSON() {
    return {
      id: this.id,
      type: this.type,
      parentId: this.parentId,
      props: { ...this.props },
      children: this.children.map(c => c.toJSON())
    };
  }

  static fromJSON(json, classMap = {}) {
    const Klass = classMap[json.type] || BaseComponent;
    const instance = new Klass({ id: json.id, parentId: json.parentId });
    instance.props = { ...json.props };
    instance.children = (json.children || []).map(c => BaseComponent.fromJSON(c, classMap));
    return instance;
  }

  destroy() {
    if (this._leaferNode) {
      this._leaferNode.remove();
      this._leaferNode = null;
    }
    this.children.forEach(c => c.destroy());
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { BaseComponent };
}
