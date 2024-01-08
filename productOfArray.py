'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''


class Solution(object):
    def product_except_self(self, nums):
        n = len(nums)

        prefix_products = [1] * n
        suffix_products = [1] * n

        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]

        result = [prefix_products[i] * suffix_products[i] for i in range(n)]

        return result


nums = [1, 2, 3, 4]
print(Solution().product_except_self(nums))
