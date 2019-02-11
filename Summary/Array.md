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

### Sorting Algo
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

* Merge sort - O(n * log n)
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

* Quick sort
  * first as pivot

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
    pivot_index = smaller_index
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



* heap sort（堆排序）
* bucket sort(O(n))（桶排序）
* count sort(计数排序)

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
* Iterative
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

#### Iterative Implementation
* left <= right
* left < right
* left + 1 < right

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
