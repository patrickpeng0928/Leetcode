class Solution:
    def findTheDifferenceBitManipulation(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import functools
        import operator
        return chr(functools.reduce(operator.xor, map(ord, s + t)))

    def findTheDifferenceBitManipulation2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for c in s + t:
            res ^= ord(c)
        return chr(res)
