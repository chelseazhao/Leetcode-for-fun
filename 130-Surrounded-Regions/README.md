130 Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

思路：宽度优先搜索。从边开始BFS遍历，将访问到的点置为'A'，表示访问过的且没有被包围的点，压入队列，循环遍历队列直到为空。最后将所有'O'置为'X'，所有'A'置为'O'