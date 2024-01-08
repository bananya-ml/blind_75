'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''


class Solution(object):
    def max_subarray_sum(self, nums):
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().max_subarray_sum(nums))
