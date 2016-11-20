class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        if num1 == None or num2 == None or len(num1) == 0 or len(num2) == 0:
            return result
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            a = int(num1[i])
            for j in range(len(num2)):
                b = int(num2[j])
                res[i + j] += a * b
        for i in range(len(res)):
            c1 = res[i] % 10
            c2 = res[i] / 10
            if i < len(res) - 1:
                res[i + 1] += c2
            result.insert(0, str(c1))
        while result[0] == '0' and len(result) > 1:
            del result[0]
        return "".join(result)
