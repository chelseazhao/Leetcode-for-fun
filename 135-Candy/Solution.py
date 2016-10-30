class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        total = 0
        descLength = 0
        preNum = 1
        beforeDesc = preNum
        if len(ratings) == 1:
            return 1
        else:
            total += 1
            for i in range(1, len(ratings)):
                if ratings[i] < ratings[i - 1]:
                    descLength += 1
                    if beforeDesc <= descLength:
                        total += 1
                    total += descLength
                    preNum = 1
                else:
                    curNum = 0
                    if ratings[i] > ratings[i - 1]:
                        curNum = preNum + 1
                    else:
                        curNum = 1
                    total += curNum
                    preNum = curNum
                    descLength = 0
                    beforeDesc = curNum
        return total
