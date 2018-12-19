class Solution(object):
	def singleNumberBitManipulation(self, nums):
		"""
		Time - O(n)
		Space - O(1)
		:type nums: List[int]
		:rtype: int
		"""
		a = 0
		for i in nums:
			a ^= i
		return a

	def singelNumberBitManipulation2(self, nums):
		"""
		Time - O(n)
		Space - O(1)
		:type nums: List[int]
		:rtype: int
		"""
		from functools import reduce
		return reduce(lambda i, j: int(i) ^ int(j), nums)

