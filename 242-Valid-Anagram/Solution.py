class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alpha_map = {}
        for ss in s:
            if ss not in alpha_map:
                alpha_map[ss] = 1
            else:
                alpha_map[ss] += 1
        for tt in t:
            if tt in alpha_map:
                alpha_map[tt] -= 1
            else:
                return False
        for alpha in alpha_map.keys():
            if alpha_map[alpha] != 0:
                return False
        return True
