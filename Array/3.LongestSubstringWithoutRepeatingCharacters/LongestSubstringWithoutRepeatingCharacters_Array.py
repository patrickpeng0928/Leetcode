class Solution(object):
    def longestUnique(self, s: 'str') -> int:
        """
        Time - O(n)
        Spacce - O(n)
        1. Define a sliding window to contain the substring withouth repeating char
        2. Using a dictionary to record the last occurance of the character in the string
        3. Iterate through string from left to right, compare length of the sliding window with the max length before.
        4. need to record the start point of the sliding window in each iteration
        """
        dict = {}
        res = 0
        start = 0
        for i, char in enumerate(s):
            if char in dict and start < i:
                # existing char in the sliding widonw
                # reset the start of the sliding window to next char of the existing char
                start = dict[char] + 1
            else:
                # no same char existing in the window
                # extend window
                # cal new length
                res = max(res, i - start + 1)
            # update the occureance of the char
            dict[char] = i
        return res


if __name__ == "__main__":
    print("Start testing ... ")
    s = Solution()
    assert s.longestUnique("abcabcbb") == 3, \
        "Failed, example: abcabcb"
    assert s.longestUnique("bbbbb") == 1, \
        "Failed, example: bbbbb"
    assert s.longestUnique("pwwkew") == 3, \
        "Failed, example: pwwkew" 
    print("All tests passed.")

