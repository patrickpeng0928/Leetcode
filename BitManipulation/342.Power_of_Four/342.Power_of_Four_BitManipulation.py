class Solution(object):
    def isPowerOfFourBitManipulation(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

    def isPowerOfFourBitManipulation2(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555 ) != 0
