class Solution(object):
	def singleNumberHashTable(self, nums):
                """
                Time - O(n)
                Space - O(n)
                :type nums: List[int]
                :rtype: int
                """
		hash_table = {}
        	for i in nums:
            		try:
                		hash_table.pop(i)
            		except:
                		hash_table[i] = 1
        	return hash_table.popitem()[0]
