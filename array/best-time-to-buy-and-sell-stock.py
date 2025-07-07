class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy_prices = prices[0]
        for i in range(len(prices)):
            res = max(res, prices[i]-buy_prices)
            if buy_prices> prices[i]:
                buy_prices = prices[i]
        return res

        