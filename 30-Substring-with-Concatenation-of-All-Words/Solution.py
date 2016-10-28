class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        words_dict = {}
        for word in words:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        length = len(words[0])
        size = len(words)
        result = []
        for i in range(len(s) - length * size + 1):
            cur_dict= {}
            j = 0
            while j < size:
                word = s[i + length * j: i + length*j + length]
                if word not in words_dict:
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > words_dict[word]:
                    break
                j += 1
            if j == size:
                result.append(i)
        return result
