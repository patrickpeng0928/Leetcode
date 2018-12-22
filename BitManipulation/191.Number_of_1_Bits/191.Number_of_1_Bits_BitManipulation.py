class Solution(object):
    def numberOfOneBitsBitManipulation(self, n):
        """
        Time - O(length(n)) = O(32)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        result = 0
        while n:
            result += (n & 1)
            n >>= 1
        return result

    def numberOfOneBitsBitManipulation2(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return bin(n).count('1')

    def numberOfOneBitsBitManipulation3(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        cnt = 0
        while n:
            cnt += 1
            n &= n - 1
        return cnt
