class Solution(object):
        def singleNumberList(self, nums):
                """
                Time - O(n^2)
                Space - O(n)
                :type nums: List[int]
                :rtype: int
                """
                no_duplicate_list = []
                for i in nums:
                        if i not in no_duplicate_list:
                                no_duplicate_list.append(i)
                        else:
                                no_duplicate_list.remove(i)
                return no_duplicate_list.pop()

