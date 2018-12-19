class Solution(object):
	def singleNumberMath(self, nums):
                """
                Time - O(n)
                Space - O(n)
                :type nums: List[int]
                :rtype: int
                """
		return 2 * sum(set(nums)) - sum(nums)
