# Depth First Search

* DFS is often preferred if we want to visit every node in the graph.
* We visit a node(a) and then iterate through each of a's neighbors.
* When visiting a node(b) that is a neighbor of a, we visit all of b's neighbors before going on to a's other neighbors.
* An exhaustively searches b's branch before any of its other neighbors.
* pre-order and other forms of tree traversal are a form of DFS.
* The key difference is that when implementing this algorithm for a graph, we must check if the node has been visited.

```python
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v,",")
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visitd = [False] * len(self.graph)
        self.DFSUtil(v, visited)
```

```python
from collections import defaultdict
class Graph:
    """
    Handling disconnected graph
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v,",")
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        V = len(self.graph)
        visitd = [False] * V
        for i in range(V):
            if not visited[i]:
                self.DFSUtil(i, visited)
```

```python
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
```

```python
def dfs(graph, sart, visited = None):
    """
    Recursive
    """
    if not visited:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
```

```python
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graphp[verste - set(path)]:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [nexts]))
```

```python
def dfs_paths(graph, start, goal, path = None):
    """
    Recursive
    """
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])
```
