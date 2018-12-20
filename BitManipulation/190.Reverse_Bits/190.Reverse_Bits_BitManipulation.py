class Solution(object):
    def reverseBitsBitManipulation(self, n):
        """
        Time - O(length(n)) = O(32)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        result = 0
        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result
