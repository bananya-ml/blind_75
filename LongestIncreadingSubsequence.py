'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        LIS = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))
