'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1 = r2 = 0
        for n in nums:
            r1, r2 = r2, max(r1 + n, r2)

        return r2


nums = [1, 2, 3, 1]
print(Solution().rob(nums))
