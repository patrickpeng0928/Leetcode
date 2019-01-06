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
### Get bit
```python
def getBit(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num
    :rtype boolean              1 or 0
    """
    return ((num & (1 << position)) != 0)
```

### Set bit
```python
def setBit(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num
    :rtype int                  an integer with 1 at position
    """
    return num | (1 << position)
```

### Clear bit
```python
def clearBit(num, position):
    """
    :type num: integer          an integer
    :type position: integer     the bit-position in the num
    :rtype int                  an integer with 0 at position
    """
    mask = ~(1 << position)
    return num & mask
```
