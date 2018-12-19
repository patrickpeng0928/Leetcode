class Solution(object):
	def singleNumberIIMath(self, nums):
                """
                Time - O(n)
                Space - O(n)
                :type nums: List[int]
                :rtype: int
                """
		return (3 * sum(set(nums)) - sum(nums)) / 2
