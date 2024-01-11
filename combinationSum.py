'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
'''


class Solution(object):
    def combinationSum4(self, nums, target):
        dp = {0: 1}

        for total in range(1, target+1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)

        return dp[target]


nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))
