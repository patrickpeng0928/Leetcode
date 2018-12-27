class Solution(object):
    def bitwiseANDOfNumbersRangeBitManipulation(self, m, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i

    def bitwiseANDOfNumbersRangeBitManipulation2(self, m, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        while m < n:
            n &= n - 1
        return n

    def bitwiseANDOfNumbersRangeBitManipulation3(self, m, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return bitwiseANDOfNumbersRangeBitManipulation3(self, m / 2, n / 2) << 1 if n > m else m
