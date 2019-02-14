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
* Implement Tree by Node (Simplified)
```python
class Node:
    def __init__(self, name = '', children = []):
        self._name = name
        self._chilren = children
```

* Implement Tree
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
    def root(self):
        return self._root

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

    def display_helper(self, identifier, level):
            print("\t" * level, "{}".format(identifier))

    def display(self, name, depth = _ROOT):
        l = 0
        self.display_helper(name, l)
        queue = list(map(lambda e: (e, l + 1), self.nodes[name].children))
        while queue:
            first = queue[0]
            node = first[0]
            lvl = first[1]
            if lvl <= depth:
                self.display_helper(node.name, lvl)
                expansion = self.nodes[name].children
                queue = list(map(lambda e: (e, lvl + 1), expansion)) + queue[1:]
            else:
                queue = queue[1:]

    def traverse(self, name, mode = _DEPTH):
        yield self.nodes[name]
        queue = self.nodes[name].children
        while queue:
            yeild queue[0]
            expansion = self.nodes[queue[0].name].children
            if mode = _DEPTH:
                queue = expansion + queue[1:0]
            if mode = _BREADTH:
                queue = queue[1:0] + expansion

    def __getitem__(self, key):
        return self.nodes[key]

    def __setitem__(self, key, item):
        assert isinstance(item, Node)
        return self.nodes[key] = item


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

    def display_helper(self, identifier, level):
        print("\t" * level, "{}".format(identifier))

    def display2(self, identifier, depth=_ROOT):
        l = 0
        self.display_helper(identifier, l)
        queue = [ m for m in map(lambda e: (e, l + 1), self[identifier].children) ]
        while queue:
            first = queue[0]
            ident = first[0]
            lvl = first[1]
            if lvl <= depth:
                self.display_helper(ident, lvl)
                expansion = self[ident].children
                queue = [ m for m in map(lambda e: (e, lvl + 1), expansion) ] + queue[1:]
            else:
                queue = queue[1:]

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

#### Trees vs Binary Trees
```
A binary tree is a tree in which each node has up to two children. Not all trees are binary trees.
```

```python
class Node:
    """
    Binary Tree
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        if self.left:
            print(self.left)
        print(self.data)
        if self.right:
            print(self.right)

    def insert(self, new_data):
        if self.data:
            if new_data < self.data:
                if self.left:
                    self.left.insert(new_data)
                else:
                    self.left = Node(new_data)
            elif new_data > self.data:
                if self.right:
                    self.right.insert(new_data)
                else:
                    self.right = Node(new_data)
        else:
            self.data = new_data
```

* A node is called a "leaf" node if it has no children.

#### Binary Trees vs Binary Search Trees
```
A binary search tree is a binary tree in which every node fits a specific ordering property: all left descendents <= n < all right descendents.Thismustbetrueforeachnoden.
```

* When given a tree question, many candidates assume the interviewer means a binary search tree. Be sure to ask.

#### Balanced vs. Unbalanced
* While many trees are balanced, not all are. Ask your interviewer for clarification here.

* Note that balancing a tree does not mean the left and right subtrees are exactly the same size (like you see under "perfect binary trees" in the following diagram).

* One way to think about it is that a "balanced" tree really means something more like "not terribly imbal­ anced:'It'sbalancedenoughtoensure0(log n)timesforinsertandfind,butit'snotnecessarilyas balanced as it could be.

* Two common types of balanced trees are **red-black trees** (pg 639) and **AVL trees** (pg 637). These are discussed in more detail in the Advanced Topics section.

#### Complete Binary Trees
```
A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it is filled left to right.
```

#### Full Binary Trees
```
A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.
```

#### Perfect Binary Trees
```
A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes.
```

* A perfect tree must have exactly (2^k - 1) nodes, (where k is the number of levels).

#### Question to Ask
* Tree or Binary tree or Binary Search Tree?
* Balanced or unbalanced?
* In an interview, do not assume a binary tree is perfect.


### Binary Tree Traverse
#### In-Order Traversal
```
In-order traversal means to "visit" (often, print) the left branch, then the current node, and finally, the right branch.
```

* When performed on a binary search tree, it visits the nodes in ascending order (hence the name"in-order").


```python
def inOrderTraversal(node = TreeNode()):
    if node:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)
```

#### Pre-Order Traversal
```
Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").
```
* In a pre-order traversal, the root is always the first node visited.

```python
def preOrderTraversal(node = TreeNode()):
    if node:
        visit(node)
        inOrderTraversal(node.left)
        inOrderTraversal(node.right)
```
#### Post-Order Traversal
```
Post-order traversal visits the current node after its child nodes (hence the name"post-order").
```

* In a post-order traversal, the root is always the last node visited.

```python
def postOrderTraversal(node = TreeNode()):
    if node:
        inOrderTraversal(node.left)
        inOrderTraversal(node.right)
        visit(node)
```

### Binary Heaps (Min-Heaps and Max-Heaps)
* Min-Heaps: elements are in ascending order
* Max-Heaps: elements are in descending order, just opposite to Min-Heaps

```
A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last level) where each node is smaller than its children. The root, therefore, is the minimum element in the tree.
```

#### Operations
* insert - O(log n), n = # of nodes in the heap
```
When we insert into a min-heap, we always start by inserting the element at the bottom. We insert at the rightmost spot so as to maintain the complete tree property.

Then, we "fix"the tree by swapping the new element with its parent, until we find an appropriate spot for the element. We essentially bubble up the minimum element.
```

* extract_min - O(log n)
```
Finding the minimum element of a min-heap is easy: it's always at the top. The trickier part is how to remove it. (In fact, this isn't that tricky.)

First, we remove the minimum element and swap it with the last element in the heap (the bottommost, rightmost element). Then, we bubble down this element, swapping it with one of its children until the min­ heap property is restored.

Do we swap it with the left child or the right child? That depends on their values. There's no inherent ordering between the left and right element, but you'll need to take the smaller one in order to maintain the min-heap ordering.

```

#### Implementation
* Max-Heaps
  * parent > children
  * array.length vs array.heap-size
  * parrent(i) = (i - 1)/2
  * left(i) = 2i + 1
  * right(i) = 2i + 2
  * arr -> heap, arr[ n/2 + 1, ...., n - 1] are leaves
  * Keep max-heap

```python
class Heap:
    def __init__(self, arr):
        self.list = arr[:]
        self.heap_size = len(arr)
        self.isMaxHeap = False
        self.build_max_heap()

    def __str__(self):
        return str(self.list)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) / 2

    def insert(self, key):
        """
        run time o(logn)
        """
        self.heap_size += 1
        self.list.append(-float("inf"))
        self.increase_key(self.heap_size - 1,key)

    def increase_key(self, i, key):
        """
        run time o(logn)
        """
        if key < self.list[i]:
            raise ValueError("new key is smaller than current key")
        self.list[i] = key
        while i>0 and self.list[self.parent(i)] < self.list[i]:
            print("i1="+str(i))
            temp = self.list[i]
            self.list[i] = self.list[self.parent(i)]
            self.list[self.parent(i)] = temp
            i = self.parent(i)
            print("i2="+str(i))

    def max_heapify(self, i):
        """
        run time: O(log n)
        the key to maintain the max-heap property
        """
        l = self.left(i)
        r = self.right(i)
        # i_m = i
        # largest = 0
        print("l="+str(l)+" r="+str(r))
        print(self.heap_size)
        largest = i
        if l < self.heap_size:
            if self.list[l] > self.list[largest]:
                largest = l
        print("r="+str(r)+" largest="+str(largest))
        if r < self.heap_size:
            if self.list[r] > self.list[largest]:
                largest = r
        print("largest="+str(largest))
        if largest != i:
            self.list[i], self.list[largest] = self.list[largest], self.list[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        run time: O(n * log n)
        """
        print(self.heap_size//2)
        for i in range(self.heap_size // 2 - 1, -1, -1):
            print("index=", str(i))
            self.max_heapify(i)
        self.isMaxHeap = True

    def extract_max(self):
        """
        build a maxheap and return the max value of it(the first element)
        also pop the first element out of the heap
        run time o(logn)
        """
        if self.heap_size < 1:
            raise ValueError("heap underflow")
        # if self.ismaxheap == False:
          # self.build_max_heap()
        maxele = self.list[0]
        self.list[0] = self.list[self.heap_size - 1]
        self.list[self.heap_size - 1] = maxele
        self.heap_size -= 1
        self.max_heapify(0)
        return maxele

    def heap_sort(self):
        """
        using recurrence to impelete, can also use for loop
        """
        if self.heap_size == 1:
            return self.list
        self.build_max_heap()
        self.list[0], self.list[self.heap_size - 1] = self.list[self.heap_size - 1], self.list[0]
        self.heap_size -= 1
        self.heap_sort()

    def heap_sort_iter(self):
        """
        iterative
        """
        if self.heap_size == 1:
            return self.list
        for i in range(self.heap_size - 1, 0, -1):
            self.list[i], self.list[0] = self.list[0], self.list[1]
            self.max_heapify(0)
            self.heap_size -= 1
            print(self.heap_size)
            print(self.list)

        print(self.list)
```


* Min-Heaps

### Tries(Prefix Trees)
