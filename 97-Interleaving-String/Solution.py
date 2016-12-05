class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        lx, ly, l = len(s1)+1, len(s2)+1, len(s3)+1
        if lx + ly - 1 != l:
            return False
        dp = [[True for _ in range(ly)] for _ in range(lx)]
        for i in range(1, lx):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, ly):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, lx):
            for j in range(1, ly):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        
        return dp[-1][-1]
