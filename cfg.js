// Generated by CoffeeScript 1.4.0
var CFGTree, Link, Value;

Value = (function() {

  function Value(stringRep, isTerminal) {
    this.stringRep = stringRep;
    this.isTerminal = isTerminal;
  }

  return Value;

})();

Link = (function() {

  function Link(source, target) {
    this.source = source;
    this.target = target;
  }

  return Link;

})();

CFGTree = (function() {

  CFGTree.numberNodes = 0;

  CFGTree.nodes = [];

  CFGTree.links = [];

  CFGTree.S_ = new Value("S", false);

  CFGTree.a = new Value("a", true);

  CFGTree.b = new Value("b", true);

  CFGTree.eps = new Value("", true);

  CFGTree.production = [[CFGTree.a], [CFGTree.b], [CFGTree.eps], [CFGTree.a, CFGTree.S_, CFGTree.a], [CFGTree.b, CFGTree.S_, CFGTree.b]];

  function CFGTree(values) {
    this.values = values;
    this.children = [];
    this.unique_id = CFGTree.numberNodes;
    CFGTree.numberNodes += 1;
    CFGTree.nodes.push(this);
  }

  CFGTree.prototype.expand = function() {
    var idx, p, tempNode, tempValues, v, _i, _len, _ref, _results;
    _ref = this.values;
    _results = [];
    for (idx = _i = 0, _len = _ref.length; _i < _len; idx = ++_i) {
      v = _ref[idx];
      if (!v.isTerminal) {
        _results.push((function() {
          var _j, _len1, _ref1, _ref2, _results1;
          _ref1 = CFGTree.production;
          _results1 = [];
          for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
            p = _ref1[_j];
            tempValues = this.values.slice(0);
            tempValues[idx] = p;
            tempValues = (_ref2 = []).concat.apply(_ref2, tempValues);
            tempNode = new CFGTree(tempValues);
            this.children.push(tempNode);
            _results1.push(CFGTree.links.push(new Link(this, tempNode)));
          }
          return _results1;
        }).call(this));
      } else {
        _results.push(void 0);
      }
    }
    return _results;
  };

  return CFGTree;

})();