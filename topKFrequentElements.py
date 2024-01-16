'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        return [x[0] for x in count.most_common(k)]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
