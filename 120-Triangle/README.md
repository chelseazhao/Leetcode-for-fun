120 Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

思路：1. 空间复杂度O(n^2) sum[i][j] = min(sum[i + 1][j], sum[i + 1][j + 1]) + triangle[i][j]
2. 空间复杂度O(n) 从下向上循环，每层res[i] = row[i] + min(res[i], res[i + 1])