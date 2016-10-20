class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''
        i = 0
        while num > 0:
            count = num / integer[i]
            num %= integer[i]
            while count > 0:
                result += roman[i]
                count -= 1
            i += 1
        return result
