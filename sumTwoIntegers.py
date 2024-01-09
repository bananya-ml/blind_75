'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])


a = 1
b = 2
print(Solution().getSum(a, b))
