class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0:
            return len2
        elif len2 == 0:
             return len1
        dis = [[0 for i in range(len1+1)] for j in range(len2+1)]
        for i in range(len2+1):
            dis[i][0] = i
        for j in range(len1+1):
            dis[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i - 1] == word2[j - 1]:
                    dis[j][i] = dis[j - 1][i - 1]
                else:
                    replace = dis[j - 1][i - 1] + 1
                    insert = dis[j - 1][i] + 1
                    delete = dis[j][i - 1] + 1
                    minimum = min(replace, insert, delete)
                    dis[j][i] = minimum
        return dis[len2][len1]
