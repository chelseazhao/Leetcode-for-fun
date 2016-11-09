class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = [(1, 1)]
        for i in range(n):
            val, factor = heapq.heappop(h)
            heapq.heappush(h, (val * 5, 5))
            if factor <= 3:
                heapq.heappush(h, (val * 3, 3))
            if factor <= 2:
                heapq.heappush(h, (val * 2, 2))
        return val
