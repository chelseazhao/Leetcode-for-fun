class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        length = len(prices)
        preMax = [0] * length
        postMin = [0] * length
        result = 0
        curMin = prices[0]
        for i in range(1, length):
            price = prices[i]
            if price < curMin:
                curMin = price
            preMax[i] = max(preMax[i - 1], price - curMin)
        curMax = prices[length - 1]
        for i in range(length - 2, -1, -1):
            if prices[i] > curMax:
                curMax = prices[i]
            postMin[i] = min(postMin[i + 1], prices[i] - curMax)
            if preMax[i] - postMin[i] > result:
                result = preMax[i] - postMin[i]
        return result
