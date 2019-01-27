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

```python
def mergeList(words = [], more = []):
    sentence = []
    for w in words:
        sentence.append(w)
    for m in more:
        sentence.apend(m)
    return sentence
```
```scala
def mergeArray(a: Array[Any], b: Array[Any]):Array[Any] = a ++ b

def mergeArray(a: Array[Any], b: Array[Any]):Array[Any] = Array.concat(a, b)

def mergeArray(
  a: collection.mutable.ArrayBuffer[Any]
  , b: Seq[Any]
):collection.mutable.ArrayBuffer[Any] = {
  a ++= b
  return a
  }

def mergeList(
  a: List[Any]
  , b: List[Any]
  ): List[Any] = a ::: b

```

### Amortized insertion runtion O(1)
Inserting N elements takes O(N) work total. Each insertion is 0(1) on average, even though some insertions take O(N) time in the worst case.

## StringBuilder

Imagine you were concatenating a list of strings, as shown below. What would the running time of this code be? For simplicity, assume that the strings are all the same length (call this x) and that there are n strings.

The total time therefore is O(x + 2x + . . . + nx). This reduces toO(xn2).

StringBuilder can help you avoid.this problem. StringBuilder simply creates a resizable array of all the strings, copying them back to a string only when necessary.

## Hash Table Collision Resolution
Essentially any hash table can have collisions. There are a number of ways of handling this.

### Chaining with Linked Lists
With this approach (which is the most common), the hash table's array maps to a linked list of items. We just add items to this linked list. As long as the number of collisions is fairly small, this will be quite efficient.

In the worst case, lookup is O(n), where n is the number of elements in the hash table. This would only happen with either some very strange data or a very poor hash function (or both).

### Chaining with Binary Search Trees
Rather than storing collisions in a linked list, we could store collisions in a binary search tree. This will bring the worst-case runtime to O(log n).

In practice, we would rarely take this approach unless we expected an extremely nonuniform distribution.

### Open Addressing with Linear Probing
In this approach, when a collision occurs (there is already an item stored at the designated index), we just move on to the next index in the array until we find an open spot. (Or, sometimes, some other fixed distance, liketheindex + 5.)

If the number of collisions is low, this is a very fast and space-efficient solution.

One obvious drawback of this is that the total number of entries in the hash table is limited by the size of the array. This is not the case with chaining.

There's another issue here. Consider a hash table with an underlying array of size 100 where indexes 20 through 29 are filled (and nothing else). What are the odds of the next insertion going to index 30? The odds are 10% because an item mapped to any index between 20 and 30 will wind up at index 30. This causes an issue called clustering.

### Quadratic Probing and Double Hashing
The distance between probes does not need to be linear. You could, for example, increase the probe distance quadratically. Or, you could use a second hash function to determine the probe distance.

## Rabin-Karp Substring Search
The brute force way to search for a substring S in a larger string B takesO(s(b- s)) time, where s is the length of S and b is the length of B. We do this by searching through the first b - s + 1 characters in B and, for each, checking if the next s characters match S.

The Rabin-Karp algorithm optimizes this with a little trick: if two strings are the same, they must have the same hash value. (The converse, however, is not true. Two different strings can have the same hash value.)

Therefore, if we efficiently precompute a hash value for each sequence of s characters within B, we can find the locations of S inO(b) time. We then just need to validate that those locations really do match S.

For example, imagine our hash function was simply the sum of each character (where space= 0, a= 1, b = 2,andsoon).IfSisearandB=doe are hearing me, we'd then just be looking for sequences where the sum is 24 (e +a+ r).This happens three times. For each of those locations, we'd check if the string really is ear.

If we computed these sums by doing hash('doe'), then hash('oe '),then hash('e a'), and soon, we would still be at O(s(b-s)) time.

Instead, we compute the hash values by recognizing that `hash('oe ') = hash('doe') - code('d') + c ode(' ')`. This takes O(b) time to compute all the hashes.

You might argue that, still, in the worst case this will take O(s(b-s)) time since many of the hash values could match. That's absolutely true-for this hash function.

In practice, we would use a better rolling hash function, such as the Rabin fingerprint. This essentially treats a string like doe as a base 128 (or however many characters are in our alphabet) number.

`hash('doe') = code('d') * 128^2 + code('o') * 128^1 + code('e') * 128^0`

This hash function will allow us to remove the d, shift the o and e, and then add in the space.

`hash('oe ') = (hash('doe') - code('d') * 128^2) * 128 + code(' ')`

This will considerably cut down on the number of false matches. Using a good hash function like this will give us expected time complexity of O(s + b), although the worst case is O(sb).

Usage of this algorithm comes up fairly frequently in interviews, so it's useful to know that you can identify substrings in linear time.

## Questions
### 1.1 Is Unique

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

* Hints

#44 Try a hash table.
#117 Could a bit vector be useful?
#132 Can you solve it in O(N log N) time? What might a solution like that look like?

* Answer
  * Ask about ASCII or Unicode String?
  * Unicode string needs more storage size
  * Immediately return false  if the string length exceeds the number of unique characters in the alphabet. After all, you can't form a string of 280 unique characters out of a 128-character alphabet.
  * It's also okay to assume 256 characters. This would be the case in extended ASCII. You should clarify your assumptions with your interviewer.

```python
def isUniqueChars(words):
    """
    Using an list to record the occurence of each character in ASCII character set

    Time complexity: O(1)
    Space complexity: O(1)

    :type words: String       a string
    :rtype boolean
    """
    if len(words) > 128: return False

    char_set = [ 0 for _ in range(128) ]
    for w in words:
        val = ord(w)
        if char_set[val]: return False
        char_set[val] = 1
    return True
```

```python
def isUniqueChars(words):
    """
    Using an dictionay to record the occurence of each character in ASCII character set

    Time complexity: O(1)
    Space complexity: O(1)

    :type words: String       a string
    :rtype boolean
    """
    if len(words) > 128: return False

    char_set = {}
    for w in words:
        if char_set.get(w):
            return False
        else:
            char_set[w] += 1
    return True
```

### 1.2 Check Permutation
* Description

Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.

* Hints:

#1 Describe what it means for two strings to be permutations of each other. Now, look at that definition you provided. Can you check the strings against that definition?

#84 There is one solution that is 0(N log N) time. Another solution uses some space, but is O(N) time.

#122 Could a hash table be useful?

#131 Two strings that are permutations should have the same characters, but in different orders. Can you make the orders the same?

* Answer
  * Is permutation comparison *case* sensitive?
  * Is *whitespace* significant?
  * lenth different? - optimization

```python
def isPermutation(a, b):
    """
    Sort both strings and compare

    Time complexity: O(n)
    Space complexity: O(1)

    :type a: String       a string
    :type b: String       a string
    :rtype boolean
    """
    if len(a) != len(b): return False

    return sorted(a) == sorted(b)
```

```python
def isPermutation(a, b):
    """
    Count occurence of each character in both string

    Time complexity: O(n)
    Space complexity: O(1)

    :type a: String       a string
    :type b: String       a string
    :rtype boolean
    """
    if len(a) != len(b): return False

    dict = {}
    for s in a:
        dict[s] = dict.get(s, 0) + 1
    for t in b:
        dict[t] = dict.get(t) - 1
        if dict[t] < 0: return False
    return True
```

### 1.3 URLify:
* Description

Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

* EXAMPLE
```
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
```

* Hints:
#53
#118

* Answer

### 1.4 Palindrome Permutation
* Description

Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

* EXAMPLE

```
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.) ```
```

* Hints

#106,
#121,
#134,
#136

### 1.5 One Away
* Description

There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

* EXAMPLE

```
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
```
* Hints

#23,
#97,
#130

### 1.6 String Compression
* Description

Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

* Hints:

#92,
#110

### 1.7 Rotate Matrix
* Description

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

* Hints:

#51,
#100

### 1.8 Zero Matrix
* Description

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

* Hints:

#17,
#74,
#102

### 1.9 String Rotation
* Description

Assumeyou have a method isSubstringwhich checks if one word is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").

* Hints:

#34,
#88,
#104

### Additional Questions:
* Object-Oriented Design (#7.12).
* Recursion (#8.3),
* Sorting and Searching (#10.9),
* C++ (#12.11),
* Moderate Problems (#16.8, #16.17, #16.22),
* Hard Problems (#17.4, #17.7, #17.13, #17.22, #17.26).
* Hints start on page 653.

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
