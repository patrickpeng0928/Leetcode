class Solution(object):
    def sumOfTwoIntegersBitManipulation(self, a, b):
        """
        Time - O(1)
        Space - O(1)
        :type a: integer
        :type b: integer
        :rtype: integer
        """
        mask = 0xFFFFFFFF
        while b:
            temp = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = temp
        return a if a <= maximum else ~(a ^ mask)

    def sumOfTwoIntegersBitManipulation2(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555 ) != 0
