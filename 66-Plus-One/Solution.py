class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        length = len(digits)
        result = [0 for i in range(length+1)]
        digits[length - 1] = digits[length - 1] + 1
        new_digits = [0] + digits
        for i in range(length, 0, -1):
            result[i] = result[i] + new_digits[i]
            if result[i] > 9:
                result[i] = result[i] - 10
                result[i - 1] = 1
        if result[0] == 0:
            return result[1:]
        else:
            return result

if __name__ == '__main__':
    digits = [1,3,4,9]
    sol = Solution()
    print sol.plusOne(digits)
            
