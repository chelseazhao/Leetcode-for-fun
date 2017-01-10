class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        result = 0
        heaters = sorted(heaters)
        houses = sorted(houses)
        i = 0
        for x in houses:
        	while i < len(heaters) - 1 and x - heaters[i] >= heaters[i + 1] - x:
        		i += 1
        	result = max(result, abs(x - heaters[i]))
        return result
