class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        dicts = {}
        height = []
        result = []
        for i in range(len(people)):
            p = people[i]
            if p[0] in dicts:
                dicts[p[0]] += (p[1], i),
            else:
                dicts[p[0]] = [(p[1], i )]
                height += p[0],
        height.sort()
        for h in height[::-1]:
            dicts[h].sort()
            for p in dicts[h]:
                result.insert(p[0], people[p[1]])
        return result
