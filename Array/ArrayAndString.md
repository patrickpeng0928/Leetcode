# Array and string

## Hash Table
```
A hash table is a data structure that maps keys to values for highly efficient lookup.
```

### Implementation - Linked Lists and Hash code function
```
We use an array of linked lists and a hash code function.
```
#### Functions
* To **insert** a key (which might be a string or essentially any other data type) and value, we do the following:
  1. First, compute the key's hash code, which will usually be an int or long. Note that two different keys could have the same hash code, as there may be an infinite number of keys and a finite number of ints.
  2. Then, map the hash code to an index in the array. This could be done with something like hash(key) % array_length. Two different hash codes could, ofcourse, map to the same index.
  3. At this index, there is a linked list of keys and values. Store the key and value in this index. We must use a linked list because of collisions: you could have two different keys with the same hash code, or two different hash codes that map to the same index.

* To **retrieve** the value pair by its key, you repeat this process. Compute the hash code from the key, and then compute the index from the hash code. Then, search through the linked list for the value with this key.

* If the number of collisions is very high, the worst case runtime is O(N), where N is the number of keys. However, we generally assume a good implementation that keeps collisions to a minimum, in which case the lookup time is O(1).


### Implementation - Balanced binary search tree
```
Implement the hash table with a balanced binary search tree.
```

* This gives us an O(log N) lookup time. The advantage of this is potentially using less space, since we no longer allocate a large array. We can also iterate through the keys in order, which can be useful sometimes.


## Arraylist & Resizable Arrays
* In some languages, arrays (often called lists in this case) are automatically **resizable**. The array or list will grow as you append items. In other languages, like Java, arrays are **fixed** length. The size is defined when you create the array.

* When you need an array-like data structure that offers dynamic resizing, you would usually use an Arraylist. An Arraylist is an array that resizes itself as needed while still providing 0(1) access. A typical implementa­ tion is that when the array is full, the array doubles in size. Each doubling takes 0(n) time, but happens so rarely that its amortized insertion time is still O(1).



## Knowledges
### Array - Sorted
#### 1D, 2D
#### Data Structure(Time/space complexity)
* Stack
* Queue
* Heap
#### Fixed length
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
#### implementation
* ArrayList
  * Add - O(n)
  * Delete - O(n)
  * Modify - O(1)
  * Lookup - O(1) / O(n)
  * Time complexity
  * Space complexity
* ArrayList vs Linked List
* szie vs capacity
#### Lazy
* edge case
* Segment Tree
#### Array operations
#### Array with Data Structure
#### Sorting Algo
* Bubble sort
* select sort
* insert sort
* combine sort（合并排序）
* quick sort
* stack sort（堆排序）
* bucket sort(O(n))（桶排序）
* count sort(计数排序)
#### Pointers
##### Two Pointers
###### one-way two pointers
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
###### Two-way two pointers
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
#### Math
* Moore Voting Algo - Leetcode 169

#### Summary
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
#### Leetcode
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

### Binary search
* Best for look up in an array
* Search element in a **sorted** array
* Stored in **sequence**

#### Implementation
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

#### Related questions
* Search, Find, Look up, etc
* Sub-Array
* 1-D Array -> 2-D Array
* 2-D Array search best solution

#### LeetCode
* 35. Search Insert Position
* 81. Search in Rotated Sorted Array II
* 300. Sub-array
* 74. Search 2-D Array
* 278, 35, 374, 34, 163, 275, 349, 350
* Rotated array: 33, 81, 153, 154
* increasing/decreasing: 354, 315, 300
* 2-D Array: 74, 240, 378, 302

#### Summary
```
Binary search - Judgement/Edge conditions
              - Implementation - Recursive
                               - Iterative
              - Rotate
              - Sub-array
              - 2-D array
```
