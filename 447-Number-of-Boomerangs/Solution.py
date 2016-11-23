class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist_map = {}
            for j in range(len(points)):
                x1 = points[j][0]
                y1 = points[j][1]
                dist = (x - x1) ** 2 + (y - y1) ** 2
                if dist in dist_map:
                    dist_map[dist] += 1
                else:
                    dist_map[dist] = 1
            for dist in dist_map.keys():
                val = dist_map[dist]
                result += val * (val - 1)
        return result
