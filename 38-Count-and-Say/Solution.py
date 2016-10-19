class Solution(object):
    def count(self, num):
        count = 1
        part = ''
        num += '#'
        for i in range(1, len(num)):
            if num[i - 1] == num[i]:
                count += 1
            else:
                part += str(count) + num[i - 1]
                count = 1
        return part
    
            
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        res = '1'
        for i in range(2, n + 1):
            res = self.count(res)
        return res
