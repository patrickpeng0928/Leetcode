# Stacks and Queues

* ins and outs of data structure

## Stack
```
A stack uses LIFO (last-in first-out) ordering.
```

### Operations
* pop(), remove the top item from the stack.
* push(item)
* peek(), return the top item of the stack
* isEmpty()

### Time complexisty vs Array
* Unlike an array, a stack does not offer constant-time access to the ith item.
*  it does allow constant­ time adds and removes, as it doesn't require shifting elements around.

### Implementation
#### Implement with a list
```python
class Stack:
    """
      Implement Stack with list in Python
      Assume the end of the list is the top element in the Stack
    """
    def __init__(self):
        self.items = []
    def isEmpty():
        return bool(self.items)
    def isEmpty_2():
        return not not self.items
    def isEmpty_3():
        """
        fastest implementation
        """
        from operator import truth
        return truth(self.items)
    def pop(self):
        return self.items.pop()
    def push(self, item):
          return self.items.append(item)
    def peek(self):
          return self.items[len(self.items) - 1]
    def size(self):
          return len(self.items)
```

```python
class Stack:
    """
      Implement Stack with list in Python
      Assume the first item of the list is the top element in the Stack
    """
    def __init__(self):
        self.items = []
    def isEmpty():
        return bool(self.items)
    def isEmpty_2():
        return not not self.items
    def isEmpty_3():
        """
        fastest implementation
        """
        from operator import truth
        return truth(self.items)
    def pop(self):
        return self.items.pop(0)
    def push(self, item):
          return self.items.insert(0, item)
    def peek(self):
          return self.items[0]
    def size(self):
          return len(self.items)
```
#### Implementation with a Linked List
```python
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def push(self, item):
        if not self.head:
            self.head = Node(item)
        else:
            newNode = Node(item)
            newNode.next = self.head
            self.head = newNode
    def pop():
        if not self.head:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def peek():
        return self.head.data
    def isEmpty():
        return not not self.head
```


### Usage
* In certain recursive algorithms, push temporary data onto a stack as you recurse, but then remove them as you backtrack.

* A stack can also be used to implement a recursive algorithm iteratively.

## Queue
```
A queue implements FIFO (first-in first-out) ordering.
```

### Operations
* add(item)
* remove(), remove the first item in the Queue
* peek()
* isEmpty()

### Implementation
#### Implementation with a Linked List
```python
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, item):
        if not self.last:
            self.head = Node(item)
            self.last = self.head
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def dequeue():
        if not self.head:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

    def peek():
        return self.head.data

    def isEmpty():
        return not not self.head
```

### Usage
* breadth-first search
  * use a queue to store a list of the nodes that we need to process.
  * Each time we process a node, we add its adjacent nodes to the back of the queue. This allows us to process nodes in the order in which they are viewed
* implement cache

## Questions
### 3.1 Three in One

Describe how you could use a single array to implement three stacks.

* Hints

#2
#12
#38
#58

### 3.2 Stack min

How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

* Hints

#27
#59
#78

### 3.3 I Stacks and Queues Stack of Plates

Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

* FOLLOW UP

Implement a function popAt(int index) which performs a pop operationon as pecificsub-stack.

* Hints

#64
#81

### 3.4 Queue via Stacks

Implement a MyQueue class which implements a queue using two stacks.

* Hints:

#98
#114

### 3.5 Sort Stack

Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

* Hints

# 15
#32
#43

### 3.6 Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure.

* Hints

#22
#56
#63

### Additional Questions
* Linked Lists (#2.6)
* Moderate Problems (#16.26)
* Hard Problems (#17.9)

### Hints start on page 653.
