class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        dp = [collections.defaultdict(int) for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                step = A[i] - A[j]
                dp[i][step] += 1
                if step in dp[j]:
                    dp[i][step] += dp[j][step]
                    res += dp[j][step]
        return res
                
