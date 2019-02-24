class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Time - O(n)
        Space - O(n)
        :type s: str
        :type k: int
        :rtype: int
        Same logic as in [3](Array/3.LongestSubstringWithoutRepeatingCharacters/Readme.md)
        """
        char_dict = {}
        start = 0
        res = 0

        for i, char in enumerate(s):
            char_dict[char] = char_dict.get(char, 0) + 1

            while len(char_dict) > 2:
                temp = s[start]
                if char_dict[temp] > 1:
                    char_dict[temp] -= 1
                else:
                    del(char_dict[temp]) # char_dict.pop(temp, None)
                start += 1
            res = max(res, i -start + 1)
        return res
