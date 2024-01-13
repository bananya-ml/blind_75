'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''


class Solution(object):
    def canJump(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        temp = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= temp:
                temp = i
        return True if temp == 0 else False


nums = [1, 0, 4]
print(Solution().canJump(nums))
