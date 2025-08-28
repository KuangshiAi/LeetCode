class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i]: the number of coins needed for amount i
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >=0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] <= amount else -1
        