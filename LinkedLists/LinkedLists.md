# Linked Lists

## Definition
```
A linked list is a data structure that represents a sequence of nodes. In a singly linked list, each node points to the next node in the linked list. A doubly linked list gives each node pointers to both the next node and the previous node.
```

* Unlike an array, a linked list does not provide constant time access to a particular "index" within the list. This means that if you'd like to find the Kth element in the list, you will need to iterate through K elements.

* The benefit of a linked list is that you can add and remove items from the beginning of the list in constant time. For specific applications, this can be useful.

* Remember that when you're discussing a linked list in an interview, you must understand whether it is a
singly linked list or a doubly linked list.

## Implementation
```python
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class SingelLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while not node:
            print(node.val)
            node = node.next

    def insertAtBeginning(self, newVal):
        newNode = Node(newVal)
        newNode.next = self.head
        self.head = newNode

    def appendToTail(newVal):
        newNode = Node(newVal)
        if not self.head:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAfterNode(self, oneNode, newVal):
        if not oneNode:
            print("The node is missing")
            return
        newNode = Node(newVal)
        newNode.next = oneNode.next
        oneNode.next = newNode

    def removeNode(self, removeVal):
        if not removeVal:
            print("Nothing to remove")
            return

        head = self.head
        if head:
            if head.val == removeVal:
                  self.head = head.next
                  head = None
                  return
        else: # head is None
            print("List is empty")
            return

        # self.head is not None,
        # and removeVal != head.value
        while not head:
            if head.val == removeVal:
                break
            else:
                prev = head
                head = head.next

        if not head:
            print("The value dosen't exist in the linked list, nothing to remove")
            return
        else:
            prev.next = head.next
            head = None

    def removeNode_2(self, removeVale):
        if not removeVal:
            print("Nothing to remove")
            return

        head = self.head
        if head.val == removeVal:
            self.head = head.next

        while not head.next:
            if head.next.val == removeVal:
                head.next.next = head.next
                return
            else:
                head = head.next
        return
```

## The "runner" Technique
```
The "runner" (or second pointer) technique is used in many linked list problems. The runner technique means that you iterate through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through.
```
* two pointers move at different pace/speed
* two pointers move from different directions

## Recursive problems
* linked lists rely on recursion
* Time complexity is at least O(n)
* Space complexity is at least O(n)

## Questions
### 2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list.

* FOLLOW UP

How would you solve this problem if a temporary buffer is not allowed?

* Hints:

#9
#40

### 2.2 Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list.

* Hints:

#8,
#25,
#41,
#67,
#126

### 2.3 Delete Middle Node

Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

* EXAMPLE
```
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks likea->b->d->e- >f
```

* Hints

#72

### 2.4 Partition

Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

* EXAMPLE
```
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
```

* Hints:
#3
#24

### 2.5 Sum Lists

You have two numbers represented by a linked list, where each node contains a single digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

* EXAMPLE
```
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. Output:2 -> 1 -> 9.Thatis,912.
```

* FOLLOW UP

Suppose the digits are stored in forward order. Repeat the above problem.

* EXAMPLE
```
Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output:9 -> 1 -> 2.Thatis,912.
```

* Hints
#7
#30
#71
#95
#109

### 2.6 Palindrome

Implement a function to check if a linked list is a palindrome.

* Hints
#5
#13
#29
#61
#101

### 2.7 Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is defined based on reference, not value.That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

* Hints
#20
#45
#55
#65
#76
#93
#111
#120
#129

### 2.8 Loop Detection

Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

* DEFINITION

Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

* EXAMPLE
```
Input: A -> B -> C -> D -> E -> C[thesameCasearlier]
Output: C
```

* Hints
#50
#69
#83
#90

### Additional Questions
* Trees and Graphs (#4.3)
* Object-Oriented Design (#7.12)
* System Design and Scal­ability (#9.5)
* Moderate Problems (#16.25)
* Hard Problems (#17.12)
* Hints start on page 653
