'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
