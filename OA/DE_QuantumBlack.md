# QA Preparation for DE - QuantumBlack
## 2/9/2019

## Arrays
Array - Sorting
      - Two pointers - one-way two pointesrs - windows
                                             - sub-array
                     - two-way two pointers
      - 2-D Array    - Flip
                     - Rotation
      - Implementation
      - Math algorithms


## Trees

## BFS

## DFS

## Binary Search
Binary search - Judgement/Edge conditions
              - Implementation - Recursive
                               - Iterative
              - Rotate
              - Sub-array
              - 2-D array
```python
def binarySearch(arr, l, r, x):
    """
    recursive version - O(log n), O(log n)
    """
    if r >= l:
        mid = l + (r - l) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def binarySearch(arr, l, r, x):
    """
    iterative version - O(log n), O(1)
    """
    while l < r:
        mid = l + (r - l) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

## Input/Output
### csv pacakge
* read

```python
import csv
with open('*.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            colmn_names = row # list
            line_count += 1
        else:
            data = row # list
    print(f'Processed {line_count} lines.')
```

* write

```python
import csv
with open('*.csv', mode='w') as csv_file:
    csv_writer = csv.writer(  csv_file
                            , delimiter=','
                            , quotechar='"'
                            , quoting=csv.QUOTE_MINIMAL
                           )

    csv_writer.writerow(['John Smith', 'Accounting', 'November'])
    csv_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

### Pandas package
* read

```python
import pandas as pd
df = pd.read_csv('*.csv')
df = pd.read_csv('*.csv', index_col='index_col')
df = pd.read_csv('*.csv', index_col='index_col', parse_dates=['date_col'])
df = pd.read_csv( '*.csv'
                , index_col = index_col_name
                , parse_dates = date_col_list
                , header = 0
                , names = col_names_list
                )
```

* write

```python
import pandas as pd
df.to_csv('*.csv')
```

## Questions
1. 给一个数列，找后一个数和前一个数的最大的差。
```python
def max_dff(xs):
    """
    brute force - O(n^2), O(1)
    """
    n = len(xs)
    if n < 2: return -1

    max_value = xs[1] - xs[0]
    for i in range(2, n):
        for j in range(0, i):
            if xs[i] - xs[j] > max_value:
                max_value = xs[i] - xs[j]
    return max_value
```

```python
def maxDiff(xs):
    """
    record both max_dff and min_element - O(n), O(1)
    """
    n = len(xs)
    if n < 2: return -1

    max_diff = xs[1] - xs[0]
    min_element = min(xs[0], xs[1])

    for i in range(2, n):
        if (xs[i] - min_element > max_diff):
            max_diff = xs[i] - min_element

        if (xs[i] < min_element):
            min_element = xs[i]
    return max_diff
```

2. 用给定的公式，根据前n天的数据，写一个function计算从第n天开始往后计算一些东
  * Time series
    * https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
    *

3. ML
4. 提供根据顺序写程序使任意数据按此规律排序
5. Statistic
6. ML
7. 给了一个表格，有一些金融相关的index并且告诉你怎么算，让你写一个函数把指定的东西算出来并且output成CSV
8. ML: 294 feature columns 6 label columns
9. 告诉你一段时期的气温，然后让你预测另一个时段期的气温，没有数据，完全是考coding逻辑，其它两道题也相似，没有数据，就让你coding解决问题
  * https://stackabuse.com/using-machine-learning-to-predict-the-weather-part-1/
  * https://stackabuse.com/using-machine-learning-to-predict-the-weather-part-2/
  * https://machinelearningmastery.com/time-series-forecast-study-python-monthly-sales-french-champagne/

10. 二分查找
11. Time series
12. Leetcode 200, 岛之间的最短距离
```python
class Solution:
    """
    dfs:
    if 1, change all its adjacent 1s to 0 until no adjacent 1s, then count 1 island
    search rest until no 1s
    """
    def numIsland(self, grid):
        """
        :type: grid: List[List[int]]
        :rtyep: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]:
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        """
        :type: grid:  List[List[int]]
        :type: i:     index of rows
        :type: j:     index of columns
        :rtyep: None
        """
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = 0
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc]:
                    self.dfs(grid, nr, nc)
```

```python
class Solution:
    """
    bfs:
    convert adjacent island to 0
    """
    def bfs(self, grid):
        """
        :type: grid:  List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        import collections
        que = collections.deque()
        res = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    res += 1
                    grid[i][j] = 0
                    que.append((i, j))
                    while que:
                        x, y = que.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny]:
                                grid[nx][ny] = 0
                                que.append((nx, ny))
        return res
```

```python
class Solution:
    """
    dfs
    """
    def countIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    count += 1
                    self.sink(grid, i, j)
        return count

    def sink(self, grid, i, j):
        if i < 0 or i >= len(grid): return
        if j < 0 or j >= len(grid[i]): return
        if not grid[i][j]: return
        grid[i][j] = 0
        self.sink(grid, i + 1, j)
        self.sink(grid, i - 1, j)
        self.sink(grid, i, j + 1)
        self.sink(grid, i, j - 1)

```

13. 两个湖之间挖 canal的最短距离（dfs 标记+bfs 找路径）， m*n 矩阵，0是湖， 1是陆，最少的1=>0使得湖联通

Leetcode 934

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

```python
class Solution:
    """
    O(A), O(A)
    Conceptually, our method is very straightforward: find both islands, then for one of the islands, keep "growing" it by 1 until we touch the second island.

    We can use a depth-first search to find the islands, and a breadth-first search to "grow" one of them. This leads to a verbose but correct solution.
    """
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        print source, target
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d - 1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d + 1))
                    done.add(nei)
```

14. lc的trapping rain water 变形.
15. supposed that your team has two separate solutions to solve a problem. In 3-5 sentences, write an email about how do you approach your manager to discuss his/her perspective on these two ideas? 就是说你们组内讨论，无法得出统一结论，让你发个邮件给manager，请求延期交付。
16. list array
17. SQL
