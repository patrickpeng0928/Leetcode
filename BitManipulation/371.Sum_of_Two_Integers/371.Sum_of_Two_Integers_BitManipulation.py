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
