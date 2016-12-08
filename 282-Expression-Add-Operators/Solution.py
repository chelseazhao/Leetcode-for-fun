class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def isLeadingZeros(num):
            return num.startswith('00') or int(num) and num.startswith('0')
        def solve(num, target, mulExpr = '', mulVal = 1):
            result = []
            if isLeadingZeros(num):
                pass
            elif int(num) * mulVal == target:
                result += num + mulExpr,
            for x in range(len(num) - 1):
                lnum = num[:x+1]
                rnum = num[x+1:]
                if isLeadingZeros(rnum):
                    continue
                right, rightVal = rnum + mulExpr, int(rnum) * mulVal
                for left in solve(lnum, target - rightVal):
                    result += left + '+' + right,
                for left in solve(lnum, target + rightVal):
                    result += left + '-' + right,
                for left in solve(lnum, target, '*' + right, rightVal):
                    result += left,
            return result
        if not num:
            return []
        return solve(num, target)
