class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        buy_price=prices[0]
        for i in range(len(prices)):
            if prices[i]>buy_price:
                res += prices[i]-buy_price
            buy_price=prices[i]
        return res