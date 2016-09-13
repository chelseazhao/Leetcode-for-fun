class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts = {}
        dicts['('] = ')'
        dicts['{'] = '}'
        dicts['['] = ']'
        res = []
        for word in s:
            if word in dicts.keys():
                res.append(word)
            else:
                if not res or dicts[res.pop()] != word:
                    return False
        if res:
            return False
        else:
            return True
