class Solution(object):
    def isPowerOfFourMath(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        if n < 1:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1

    def isPowerOfFourMath2(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4 == 0:
            return self.isPowerOfFourMath2(n / 4)
        else
            return False

    def isPowerOfFourMath3(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        return n in nums

    def isPowerOfFourMath4(self, n):
        """
        Time - O(1)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        return n > 0 and 4 ** int(math.log(n, 4)) == n
