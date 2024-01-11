'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
'''


class Solution(object):
    def rob(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        r1 = r2 = 0
        for n in nums:
            r1, r2 = r2, max(r1 + n, r2)

        return r2


nums = [2, 3, 2]
print(Solution().rob(nums))
