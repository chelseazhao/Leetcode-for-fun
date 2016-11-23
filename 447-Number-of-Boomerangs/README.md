447 Number of Boomrangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000](inclusive).

思路：使用HashMap，时间复杂度O(n^2)。循环记录第i个点与每个点的距离，key为距离，value为个数，距离相同的点归为一类，用val * (val - 1)得到不同数组的个数。