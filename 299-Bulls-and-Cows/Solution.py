class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        nums1 = map(int, secret)
        nums2 = map(int ,guess)
        length = len(secret)
        l1 = [0] * 10
        l2 = [0] * 10
        for i in range(length):
        	if nums1[i] == nums2[i]:
        		bulls += 1
        	else:
        		l1[nums1[i]] += 1
        		l2[nums2[i]] += 1
        cows = sum(map(min, zip(l1, l2)))
        return '%dA%dB' % (bulls, cows)