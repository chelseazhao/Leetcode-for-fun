import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_sale = sys.maxint
        max_profit = 0
        for price in prices:
            if price < min_sale:
                min_sale = price
            profit = price - min_sale
            if profit > max_profit:
                max_profit = profit
        return max_profit
