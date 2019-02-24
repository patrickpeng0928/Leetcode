class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Time - O(nlog n)
        Space - O(n)
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k: return 0
        c = min(set(s), key=s.count) ## 按照count排序
        if s.count(c) >= k:
            return len(s) ## 都满足
        return max(self.lengthOfLongestSubstringKDistinct(t, k) for t in s.split(c))
