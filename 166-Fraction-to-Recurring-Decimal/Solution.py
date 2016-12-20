class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if numerator / denominator < 0:
            result += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator / denominator)
        if numerator % denominator == 0:
            return result
        result += "."
        numerator %= denominator
        i = len(result)
        remainder = {}
        while numerator != 0:
            if numerator not in remainder.keys():
                remainder[numerator] = i
            else:
                i = remainder[numerator]
                result = result[:i] + "(" + result[i:] + ")"
                return result
            numerator = numerator * 10
            result += str(numerator / denominator)
            numerator = numerator % denominator
            i += 1
        return result
