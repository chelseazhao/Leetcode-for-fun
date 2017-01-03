class UF(object):
    def __init__(self, grid):
        self.count = 0
        self.parent = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m * n):
            self.parent.append(i)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.count += 1


    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        else:
            self.parent[px] = py
            self.count -= 1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        uf = UF(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i - 1][j] == '1':
                        uf.union(i * n + j, (i - 1) * n + j)
                    if i < m - 1 and grid[i + 1][j] == '1':
                        uf.union(i * n + j, (i + 1) * n + j)
                    if j > 0 and grid[i][j - 1] == '1':
                        uf.union(i * n + j, i * n + j - 1)
                    if j < n - 1 and grid[i][j + 1] == '1':
                        uf.union(i * n + j, i * n + j + 1)
        return uf.count

