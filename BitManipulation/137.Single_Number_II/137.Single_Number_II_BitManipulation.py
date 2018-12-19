class Solution(object):
	def singleNumberIIBitManipulation(self, nums):
		"""
		Time - O(n)
		Space - O(1)
		:type nums: List[int]
		:rtype: int
		"""
		one, two, three = 0, 0, 0
		for num in nums:
			two |= one & num
			one ^= num
			three = one & two
			one &= ~three
			two &= ~three
		return one

	def singleNumberIIBitManipulation2(self, nums):
		"""
		Time - O(n)
		Space - O(1)
		:type nums: List[int]
		:rtype: int
		"""
		one, two, three = 0, 0, 0
		for num in nums:
			three = two & num
			two |= one & num
			one ^= num
			one &= ~three
			two &= ~three
		return one
