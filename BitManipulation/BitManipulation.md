# Bit Manipulation
## Operations
```
0110 + 0010 = 1000
0011 + 0010 = 0101
0110 - 0011 = 0011
1000 - 0110 = 0010
0011 * 0101 = 1111
0011 * 0011 = 1001
1101 >> 2 = 0011
1101 ^ 0101 = 1000
0110 + 0110 = 0110 * 2 = 0110 << 1 = 1100
0100 * 0011 = 0011 * 0100 = 0011 * 4 = 0011 << 2 = 1100
1101 ^ (~1101) = 1111: a ^(~a) = 1
1011 & (~0 << 2) = 1000: ~0 = 1111
```

## Bit Facts and Tricks
```
x ^ 0s = x
x ^ 1s = ~x
x ^ x = 0
x & 0s = 0
x & 1s = x
x & x = x
x | 0s = x
x | 1s = 1s
x | x = x
```

* what's happening on one bit never impacting the other bits

## Two's Complement and Negative Numbers
* Two's complement representation
```
pos = 0 + positive number
neg = 1 + two's complement value of absolute value
```

* two's complement of N-bit number = the complement of the number with respect to 2^n

```
n-bit -K in binary = 1 concate ((2 ^ (n-1) - K) => binary)

Example:
4-bit -3 = 1 concate ((2^3 - 3) => 101) = 1101
```

## Arithmetic vs Logical Right Shift
* arithmetic right shift(>>) = /2, shift values to the right but fill in the new bits with the value of the sign bit.

* logical right shift(>>>) = shift the bits and put a 0 in the most significant bit.

* shift infinity
  * \>> => -1 (11111111)
  * \>>> => 0 (00000000)

## Common Bit Tasks: Getting and Setting
### Get Bit
```python
def getBit(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num, from 0 (right most)
    :rtype boolean              1 or 0
    """
    return ((num & (1 << position)) != 0)
```

### Set Bit
```python
def setBit(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num, from 0 (right most)
    :rtype int                  an integer with 1 at position
    """
    return num | (1 << position)
```

### Clear Bit
```python
def clearBit(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num, from 0 (right most)
    :rtype int                  an integer with 0 at position
    """
    mask = ~(1 << position)
    return num & mask

def clearBitsFromMostSignificantBitThroughI(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num, from 0 (right most)
    :rtype int                  an integer with 0 from most significant bit to position(inclusive)
    """
    mask = (1 << position) - 1
    return num & maks

def clearBitsFromIThrough0(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num
    :rtype int                  an integer with 0 from position to end
    :example:
    """
    mask = (-1 << (position + 1))
    return num & maks
```

### Update Bit
```python
def updateBit(num, position, bitIs1):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num, from 0 (right most)
    :type bitIs1: booleawn      the bit is 1 or 0 at position after update
    :rtype int                  an integer with value at position
    """
    value = 1 if bitIs1 else 0
    mask = 1 << position
    return (num & ~mask) | (value << position)

```

### Masks
|                      Explanation                      | Shifting Pattern |     Example     |
| ----------------------------------------------------- | ---------------- | --------------- |
| 1 at i, other 0s                                      | `1 << i`         | i = 3, 00100000 |
| 0 at i, other 1s                                      | `~(1 << i)`      | i = 3, 11011111 |
| 1s after i, other 0s<br> 0s from MSB to i (inclusive) | `(1 << i) - 1`    | i = 3, 00000111 |
| 0s after i (inclusive), other 1s                      | `-1 << (i + 1)`   | i = 3, 11110000 |

## Questions
### 5.1 Insertion:
* Description

You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

* EXAMPLE
```
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output:N = 10001001100
```

******
* Hints:

#137 Break this into parts. Focus first on clearing the appropriate bits.

#169 To clear the bits, create a "bit mask"that looks like a series of 1s, then Os, then 1s.

#215 It's easy to create a bit mask of Os at the beginning or �nd. But how do you create a bit mask with a bunch of zeroes in the middle?Do it the easy way: Create a bit mask for the left side and then another one for the right side.Then you can merge those.

******
* Answer
```python
def insertion(n, m, i, j):
    """
    :type n: integer          an 32-bit number
    :type m: integer          an 32-bit number
    :type i: integer          bit position
    :type j: integer          bit position
    :rtype int                n with m from j to i
    """
    # create mast like 11100011
    # create left part and right part, and then left | right
    left = -1 << (j + 1) # 11100000
    rght = (1 << i) - 1  # 00000011
    mask = left | right  # 11100011
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted
    # n & ((-1 << (j + 1)) | ((1 << i) - 1)) | (m << i)
```

### 5.2 Binary to String
* Description

Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR."

******
* Hints:

#143 To wrap your head around the problem, try thinking about how you'd do it for integers.

#167 In a number like .893 (in base 10), what does each digit signify? What then does each digit in .10010 signify in base 2?

#173 A number such as .893 (in base 10) indicates `8 * 10^-1 + 9 * 10^-2 + 3 * 10^-3`. Translate this system into base 2.

#269 How would you get the first digit in .893? If you multiplied by 10, you'd shift the values over to get 8.93. What happens if you multiply by 2?

#297 Think about what happens for values that can't be represented accurately in binary.

******
* Answer
```python
def binaryReal2String(n):
    """
    :type n: double           (0, 1)
    :rtype int                32-bit binary or ERROR.
    """
    if n >= 1 or n <= 0: return "ERROR"
    res = ['.']
    while n > 0:
      if len(res) >= 32:
        return "ERROR"
      tmp = n * 2
      if tmp >= 1:
        res.append('1')
        n = tmp - 1
      else:
        res.append('0')
        n = tmp
    return ''.join(res)
```

### 5.3 Flip Bit to Win
* Description

You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.

* EXAMPLE
```
Input: 1775 (or: 11011101111)
Output: 8
```
* Hints:

#159, Start with a brute force solution. Can you try all possibilities?

#226, Flipping a O to a 1 can merge two sequences of 1s-but only if the two sequences are separated by only one 0.

#374, Each sequence can be lengthened by merging it with an adjacent sequence (if any) or just flipping the immediate neighboring zero. You just need to find the best choice.

#352, Try to do it in linear time, a single pass, and 0(1) space.

* Answer

```python
def flipBit(num):
    """
    :type num: interger
    :rtype: int
    Brut force: DP
    11100011011111
    """

```

### 5.4 Next Number
* Description

Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.

* Hints:

#747, #7 75, #242,#372,#339,#358,#375,#390

### 5.5 Debugger
* Description

Explain what the following code does: ((n & (n-1)) == 0).

* Hints:

#757,#202,#267,#302,#346,#372,#383,#398

### 5.6 Conversion
* Description

Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

* EXAMPLE
```
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
```

* Hints:

#336,#369

### 5.7 Pairwise Swap
* Description

Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

* Hints:

#745,#248,#328,#355

### 5.8 Draw Line
* Description

A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows). The height of the screen, of course, can be derived from the length of the array and the width. Implement a function that draws a horizontal line from (xl, y) to ( x2, y).

The method signature should look something like:

drawline(byte[] screen, int width, int xl, int x2, int y)

* Hints:

#366,#387,#384,#397

### Additional Questions
* Description

Arrays and Strings (#1.1, #1.4, #1.8), Math and Logic Puzzles (#6.1O), Recursion (#8.4, #8.14), Sorting and Searching (#10.7, #10.8), C++ (#12.10), Moderate Problems (#16.1, #16.7), Hard Problems (#17.1).
