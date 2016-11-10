# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n
        while 1:
            mid = begin + (end - begin) / 2
            num = guess(mid)
            if num == 0:
                return mid
            elif num == -1:
                end = mid - 1
            elif num == 1:
                begin = mid + 1
        return mid
    
