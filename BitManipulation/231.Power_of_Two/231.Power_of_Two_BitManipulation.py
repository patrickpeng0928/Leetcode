class Solution(object):
    def powerOfTwoBitManipulation(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        if n < 1:
            return False
        while n % 2 == 0:
            n >>= 1
        return True if n == 1 else False

    def powerOfTwoBitManipulation2(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return n > 0 and not n & (n - 1)
