class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        index = len(a) if len(a)>len(b) else len(b)
        result = [0 for i in range(index+1)]
        a = a.rjust(index, '0')
        b = b.rjust(index, '0')
        for i in range(index - 1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                result[i + 1] = result[i + 1] 
            elif a[i] == '1' and b[i] == '1':
                result[i + 1] = result[i + 1]
                result[i] = 1
            else:
                result[i + 1] = result[i + 1] + 1
                if result[i + 1] == 2:
                    result[i + 1] = 0
                    result[i] = 1
        re_result = ""
        start = 1 if result[0] == 0 else 0
        for i in range(start, index + 1):
            re_result += str(result[i])
        return re_result
if __name__ == '__main__':
    a = "0"
    b = "0"
    sol = Solution()
    print sol.addBinary(a, b)
        
