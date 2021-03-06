# Array Related
## Array - Sorted
### 1D, 2D
### Data Structure(Time/space complexity)
* Stack: LIFO
* Queue: FIFO
* Heap: Tree, max-Heap, min-Heap

### Fixed length

### Operations
#### Add
* at the end, efficient
* otherwise

#### Delete
* at the end, efficient
* otherwise

#### Modify
* efficient

#### Lookup
* efficient
* indexing
* binary search
* sorting

### Implementation
* ArrayList
  * Add - O(n)
  * Delete - O(n)
  * Modify - O(1)
  * Lookup - O(1) / O(n)
  * Time complexity
  * Space complexity
* ArrayList vs Linked List
* size vs capacity

### Lazy
* edge case
* Segment Tree

### Array with Data Structure
* [Python Big O](https://wiki.python.org/moin/TimeComplexity)

### Sorting Algo

#### [Big O](http://bigocheatsheet.com)

<table class="table table-bordered table-striped">
  <tbody>
      <tr>
        <th>Algorithm</th>
        <th colspan="3">Time Complexity</th>
        <th>Space Complexity</th>
      </tr>
      <tr>
        <th></th>
        <th>Best</th>
        <th>Average</th>
        <th>Worst</th>
        <th>Worst</th>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Quicksort">Quicksort</a></td>
        <td><code class="orange">Ω(n log(n))</code></td>
        <td><code class="orange">Θ(n log(n))</code></td>
        <td><code class="red">O(n^2)</code></td>
        <td><code class="yellow-green">O(log(n))</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Merge_sort">Mergesort</a></td>
        <td><code class="orange">Ω(n log(n))</code></td>
        <td><code class="orange">Θ(n log(n))</code></td>
        <td><code class="orange">O(n log(n))</code></td>
        <td><code class="yellow">O(n)</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Timsort">Timsort</a></td>
        <td><code class="yellow">Ω(n)</code></td>
        <td><code class="orange">Θ(n log(n))</code></td>
        <td><code class="orange">O(n log(n))</code></td>
        <td><code class="yellow">O(n)</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Heapsort">Heapsort</a></td>
        <td><code class="orange">Ω(n log(n))</code></td>
        <td><code class="orange">Θ(n log(n))</code></td>
        <td><code class="orange">O(n log(n))</code></td>
        <td><code class="green">O(1)</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Bubble_sort">Bubble Sort</a></td>
        <td><code class="yellow">Ω(n)</code></td>
        <td><code class="red">Θ(n^2)</code></td>
        <td><code class="red">O(n^2)</code></td>
        <td><code class="green">O(1)</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Insertion_sort">Insertion Sort</a></td>
        <td><code class="yellow">Ω(n)</code></td>
        <td><code class="red">Θ(n^2)</code></td>
        <td><code class="red">O(n^2)</code></td>
        <td><code class="green">O(1)</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Selection_sort">Selection Sort</a></td>
        <td><code class="red">Ω(n^2)</code></td>
        <td><code class="red">Θ(n^2)</code></td>
        <td><code class="red">O(n^2)</code></td>
        <td><code class="green">O(1)</code></td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Tree_sort">Tree Sort</a></td>
        <td><code class="orange">Ω(n log(n))</code></td>
        <td><code class="orange">Θ(n log(n))</code></td>
        <td><code class="red">O(n^2)</code></td>
        <td><code class="yellow">O(n)</code></td>
      </tr>
      <tr>
        <td><a href="http://en.wikipedia.org/wiki/Shellsort">Shell Sort</a></td>
        <td><code class="orange">Ω(n log(n))</code></td>
        <td><code class="red">Θ(n(log(n))^2)</code></td>
        <td><code class="red">O(n(log(n))^2)</code></td>
        <td><code class="green">O(1)</code></td>
      </tr>
      <tr>
        <td><a rel="tooltip" title="Only for integers. k is a number of buckets" href="http://en.wikipedia.org/wiki/Bucket_sort">Bucket Sort</a></td>
        <td><code class="green">Ω(n+k)</code></td>
        <td><code class="green">Θ(n+k)</code></td>
        <td><code class="red">O(n^2)</code></td>
        <td><code class="yellow">O(n)</code></td>
      </tr>
      <tr>
        <td><a rel="tooltip" title="Constant number of digits 'k'" href="http://en.wikipedia.org/wiki/Radix_sort">Radix Sort</a></td>
        <td><code class="green">Ω(nk)</code></td>
        <td><code class="green">Θ(nk)</code></td>
        <td><code class="green">O(nk)</code></td>
        <td><code class="yellow">O(n+k)</code></td>
      </tr>
      <tr>
        <td><a rel="tooltip" title="Difference between maximum and minimum number 'k'" href="https://en.wikipedia.org/wiki/Counting_sort">Counting Sort</a></td>
        <td><code class="green">Ω(n+k)</code></td>
        <td><code class="green">Θ(n+k)</code></td>
        <td><code class="green">O(n+k)</code></td>
        <td><code class="yellow">O(k)</code></td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Cubesort">Cubesort</a></td>
        <td><code class="yellow">Ω(n)</code></td>
        <td><code class="orange">Θ(n log(n))</code></td>
        <td><code class="orange">O(n log(n))</code></td>
        <td><code class="yellow">O(n)</code></td>
     </tr>
  </tbody>
</table>

* Bubble sort

```python
def bubbleSort(arr):
    """
    O(n^2), O(1)
    Swap the adjacent elements if in wrong order
    in place sorting
    """
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

```

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j  in range(i):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

* Select sort

```python
def selectionSort(arr):
    """
    O(n^2), O(1)
    select the minimum from unsorted part and insert to the sorted subarray
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
```

* Insert sort

```python
def insertSort(arr):
    """
    O(n^2), O(1)
    insert the first in the unsorted part and insert to the sorted subarray
    """
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def insertionSort(arr):
    """
    Move elements of arr[0..i-1], that are
    greater than key(arr[i]), to one position ahead (+1)
    of their current position
    """
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

* Merge sort - O(n * log n) - Linked Lists
* Recursive Merge Sort

```python
# Recursive Merge Sort
def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    k = 0
    nl, nr = len(left), len(right)
    while (k < nl + nr):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        k += 1
        if not left or not right:
            result.extend(left or right)
            k += len(left) or len(right)
    return result

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    middle = int(n / 2)
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left, right)

```

* Iterative Merge Sort
```python
def mergeSort(lst1, lst2):
    lst1.sort()
    lst2.sort()
    result = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    result.extend(lst1 or lst2)
    return result
```

* Quick sort - O(n * log n), O(1) - Array

  * first as pivot

```python
def quickSort(arr):
    """
    Recursive, first as pivot
    """
    if not arr:
        return []
    pivot   = arr[0]
    left    = [ x for x in arr if x < pivot ]
    middle  = [ x for x in arr if x == pivot ]
    right   = [ x for x in arr if x > pivot ]
    return quickSort(left) + middle + quickSort(right)
```

```python
def partition(arr, low, high):
    """
    first element is pivot
    low: index of first element
    high: index of last element
    """
    pivot = arr[low]
    smaller_index = low
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            smaller_index += 1
            arr[smaller_index], arr[i] = arr[i], arr[smaller_index]
    pivot_index = smaller_index + 1
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    return pivot_index
```

  * last as pivot

```python
def partition(arr, low, high):
    """
    last element is pivot
    low: index of first element
    high: index of last element
    """
    pivot = arr[high]
    smaller_index = low - 1
    for i in range(low, high):
        if arr[i] < pivot:
            smaller_index += 1
            arr[smaller_index], arr[i] = arr[i], arr[smaller_index]
    pivot_index = smaller_index + 1
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return pivot_index
```

  * random as pivot

```python
def partitoin(arr, low, high):
    """
    Generate a random number between low and high
    swap it with low
    Then do it as 'low as pivot'
    """
    import random
    random_index = random.randint(low, high)
    arr[low], arr[random_index] = arr[random_index], arr[low]
    # low as pivot
    pivot = arr[low]
    smaller_index = low
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            smaller_index += 1
            arr[smaller_index], arr[i] = arr[i], arr[smaller_index]
    pivot_index = smaller_index
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    return pivot_index
```

  * median as pivot

```python
def median(arr, i, j, k):
    n = len(arr)
    if i > n or j > n  or k > n:
        return -1
    if arr[i] < arr[j]:
        return i if arr[k] < arr[i] else k if arr[k] < arr[j] else j
    else:
        return i if arr[i] < arr[k] else k if arr[j] < arr[k] else j

def partition(arr, low, high):
    """
    median element is pivot
    low: index of first element
    high: index of last element
    find median and exchange it with lowest element, then use lowest element as pivot
    """
    middle = low + (high - low) / 2
    median_index = median(arr, low, middle, high)
    arr[low], arr[median_index] = arr[median_index], arr[low]

    pivot = arr[low]
    smaller_index = low
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            smaller_index += 1
            arr[smaller_index], arr[i] = arr[i], arr[smaller_index]
    pivot_index = smaller_index
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    return pivot_index
```


```python
def quickSortHelper(arr, low, high):
    """
    low: index of first element
    high: index of last element
    """
    if low < high:
        pi = partition(arr, low, high)
        quickSortHelper(arr, low, pi - 1)
        quickSortHelper(arr, pi + 1, high)

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
```

* QuickSort Iterative

```python
def quickSort(arr):
    """
    Using Stack
    """
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(arr[-1])
    stack.append(arr[0])
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
```


* heap sort（堆排序）

```python
def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i
    n is size of heap
    """
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    """
    Heap sort an array of given size
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
```

```python
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
```


* bucket sort(O(n))（桶排序）

```
Bucket sort is mainly useful when input is uniformly distributed over a range.
```

```python
def bucketSort(xs, n):
    """
    n buckets - O(len(xs) + n)
    """
    arr = []
    slot_num = n
    for in range(slot_num):
        arr.append([])
    for j in xs:
        bucket_index = int(slot_num * j)
        arr[bucket_index].append(j)
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    result = [ inner for outer in arr for inner in outer ]
    return result

def insertionSort(xs):
    for i in range(1, len(xs)):
        up = xs[i]
        j = i - 1
        while j >= 0  and xs[j] > up:
            xs[j + 1] = xs[j]
            j -= 1
        xs[j + 1] = up
    return xs
```

* count sort(计数排序)

```python
def countSort(xs, k):
    """
    n interger between 0 and k - O(n + k)
    """
    n=len(xs)
    result=[0 for i in range(n)]
    c=[0 for i in range(k + 1)]
    for i in xs:
        c[i] += 1
    for i in range(1, len(c)):
        c[i] = c[i - 1] + c[i]
    for i in xs:
        result[c[i] - 1] = i
        c[i] -= 1
    return result

```

### Pointers
#### Two Pointers
##### one-way two pointers
```python
result = []
temp = []
for i in range(n):
  ...
```
* windows
  * sorted by the start of windows
  * end of previous window & start of next window
* scanning line algo
  * computing graphic
  * sweep line(多边形填充)
  * **scan in one direction**
  * Leetcode 253
* sub-array
  * Leetcode 209
  * 前缀和/前缀积
  * 进行中处理
  * 分段式处理

```pyton
for i in range(n):
  nums[i] += nums[i - 1]
```
##### Two-way two pointers
```python
left, right = 0, n - 1
res = []
while (left < right):
    ...
```
* Leetcode 11
* 2D-Array
  * left-right flip
  * up-down flip
  * diagnose flip
  * Leetcode 48
  * spiral order - rotation

### Math
* Moore Voting Algo - Leetcode 169

### Summary
```
Array - Sorting
      - Two pointers - one-way two pointesrs - windows
                                             - sub-array
                     - two-way two pointers
      - 2-D Array    - Flip
                     - Rotation
      - Implementation
      - Math algorithms
```
### Leetcode
* Sorting
  * 75, 283, 215, 287, 334, 300, 88, 387, 164, 347, 243, 244, 245
* One-way two pointers
  * Array operations: 26, 27, 80
  * Windows: 56, 57, 252, 253
  * Scanning line: 163, 228
  * Sub-array: 53, 152, 209, 238, 325
* Two-way two Pointers
  * 11, 42
* 2-D array
  * 36, 37, 48, 54, 59, 73, 289, 311
* Implementation
  * 189, 280, 376, 274, 229, 277, 370, 296
* Math algo
  * 134, 169
* Others
  * 321, 324, 327

## Binary search
* Best for look up in an array
* Search element in a **sorted** array
* Stored in **sequence**

### Implementation
* Recursive

```python
def binarySearch(arr, l, r, x):
    """
    Recursive
    """
    if r >= l:
        mid = (l - r) / 2 + r
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
```

* Iterative
  * left <= right

```python
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

  * left < right

```python
def binarySearch(arr, l, r, x):
    """
    """
    while l < r:
        mid = l + (r - l) / 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid

    if l == r and arr[l] == x:
        return l
    else:
        return - (l + 1)

```

  * left + 1 < right

```python
def binarySearch(arr, l, r, x):
    while l + 1 < r:
        mid = l + (r - l) / 2
        if arr[mid] == x
            return mid
        elif arr[mid] < x:
            l = mid
        else:
            r = mid
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return -1
```

* Importance:

```
mid = (right - left) / 2 + left
```
* Note:
```
right + left > Integer.MAX_VALUE (Overflow)
```
* Time complexity: O(log n)
* Space complexity: O(log n)

### Related questions
* Search, Find, Look up, etc
* Sub-Array
* 1-D Array -> 2-D Array
* 2-D Array search best solution

### LeetCode
* 35. Search Insert Position
* 81. Search in Rotated Sorted Array II
* 300. Sub-array
* 74. Search 2-D Array
* 278, 35, 374, 34, 163, 275, 349, 350
* Rotated array: 33, 81, 153, 154
* increasing/decreasing: 354, 315, 300
* 2-D Array: 74, 240, 378, 302

### Summary
```
Binary search - Judgement/Edge conditions
              - Implementation - Recursive
                               - Iterative
              - Rotate
              - Sub-array
              - 2-D array
```
