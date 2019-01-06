class Solution:
    def findTheDifferenceArray(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - 97] += 1
        for c in t:
            letters[ord(t) - 97] -= 1
        for i in range(26):
            if letters[i] < 0:
                return chr(i + 97)

    def findTheDifferenceArray2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = {}
        for c in s:
            letters[c] = letters.get(c, 0) + 1
        for c in t:
            if c not in letters:
                return c
            else:
                letters[c] -= 1
            if letters[c] < 0
                return c
