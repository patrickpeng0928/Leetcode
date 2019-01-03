class Solution(object):
    def powerOfTwoBitString(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return bin(n).count('1') == 1
