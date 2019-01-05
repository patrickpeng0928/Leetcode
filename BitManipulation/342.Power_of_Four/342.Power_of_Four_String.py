class Solution(object):
    def isPowerOfFourString(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return n > 0 and bin(n).count('1') == 1 and bin(n).count('0') % 2 == 1
