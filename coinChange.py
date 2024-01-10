class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        '''
        1. Sort the array in descending order
        2. Iterate through the array
        3. Add the first element to the result until the sum of the result list is greater than or equal to the amount
        4. If equal, return the length of the result list
        5. If greater, remove the last element from the result list and add the next element from the array
        6. Repeat steps 4 and 5 until the amount is reached or the array is exhausted
        7. If the array is exhausted, return -1
        '''
        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1


coins = [186, 419, 83, 408]
amount = 6249
print(Solution().coinChange(coins, amount))
