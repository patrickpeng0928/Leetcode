class Solution(object):
    def powerOfTwoBitMath(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        if n < 1:
            return false
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False
