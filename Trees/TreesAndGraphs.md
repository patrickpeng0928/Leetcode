# Trees and Graphs

* the worst case and average case time may vary wildly, and we must evaluate both aspects of any algorithm.

## Trees
### Type of Trees
#### Recursive explanation

```
A tree is a data structure composed of nodes.
```

* Each tree has a root node. (Actually, this isn't strictly necessary in graph theory, but it's usually how we use trees in programming, and especially programming interviews.)

* The root node has zero or more child nodes.

* Each child node has zero or more child nodes, and so on.

* The tree cannot contain cycles.

* The nodes may or may not be in a particular order

* The nodes could have any data type as values

* The nodes may or may not have links back to their parent nodes.

##### Implementation
```python
class Tree:
    """
    Generic Tree Model - by Single Tree class
    """
    def __init__(self, name = 'root', children = []):
        self.name = name
        self.children = []
        for child in children:
            self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
```

```python
class Node:
    def __init__(self, name = '', children = []):
        self._name = name
        self._children = children

    @property
    def name(self):
        return self._name

    @property
    def children(self):
        return self._children

    def add_child(sefl, newNode):
        assert isinstance(newNode, Node)
        self._children.append(newNode)

(_ROOT, _DEPTH, _BREADTH) = range(3)

class Tree:
    """
    Generic Tree Model - Node class and Tree class
    """
    def __init__(self, root = None):
        self._root = None
        self._nodes = {}
        if not root:
            self._root = root.name
            self._nodes[root.name] = root
            for child in root.children:
                self.add_node(child, root.name)

    @property
    def nodes(self):
        return self._nodes

    def add_node(self, newNode, parent = None):
        assert isinstance(newNode, Node)
        self._nodes[newNode.name] = newNode
        if not parent:
            self._nodes[parrent].add_child(newNode)

    def __repr__(self):
        return self._nodes

    def display(self, name, depth = _ROOT):
        # TODO: Not clear
        children = self._nodes[name].children
        if depth = _ROOT:
            print("{}".format(name))

    def traverse(self, name, mode = _DEPTH):
        yield self._nodes[name]
        queue = self._nodes[name].children
        while queue:
            yeild queue[0]
            expansion = self._nodes[queue[0].name].children
            if mode = _DEPTH:
                queue = expansion + queue[1:0]
            if mode = _BREADTH:
                queue = queue[1:0] + expansion

    def __getitem__(self, key):
        return self._nodes[key]

    def __setitem__(self, key, item):
        assert isinstance(item, Node)
        return self._nodes[key] = item


```

```python
class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    def add_child(self, identifier):
        self.__children.append(identifier)

(_ROOT, _DEPTH, _BREADTH) = range(3)

class Tree:

    def __init__(self):
        self.__nodes = {}

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node

        if parent is not None:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=_ROOT):
        children = self[identifier].children
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("\t"*depth, "{0}".format(identifier))

        depth += 1
        for child in children:
            self.display(child, depth)  # recursive call

    def traverse(self, identifier, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from
        # 'Essential LISP' by John R. Anderson, Albert T. Corbett,
        # and Brian J. Reiser, page 239-241
        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children
            if mode == _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode == _BREADTH:
                queue = queue[1:] + expansion  # width-first

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item
```

### Trees vs Binary Trees
