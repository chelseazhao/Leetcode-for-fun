304 Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:

    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

思路：动态规划，时间复杂度O(mn)，空间复杂度O(1)。将a(m)(n)转存为S(m)(n)，S(m)(n) = a(m)(n) + a(m-1)(n) + a(m)(n-1) - a(m-1)(n-1)，要求的S(m1->m2)(n1->n2) = S(m2)(n2) - S(m1-1)(n2) - S(m2)(n1-1) + S(m1-1)(n1-1)