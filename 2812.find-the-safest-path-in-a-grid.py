#
# @lc app=leetcode.cn id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#
# https://leetcode.cn/problems/find-the-safest-path-in-a-grid/description/
#
# algorithms
# Medium (24.55%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 10.5K
# Testcase Example:  '[[1,0,0],[0,0,0],[0,0,1]]'
#
# You are given a 0-indexed 2D matrix grid of size n x n, where (r, c)
# represents:
# 
# 
# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# 
# 
# You are initially positioned at cell (0, 0). In one move, you can move to any
# adjacent cell in the grid, including cells containing thieves.
# 
# The safeness factor of a path on the grid is defined as the minimum manhattan
# distance from any cell in the path to any thief in the grid.
# 
# Return the maximum safeness factor of all paths leading to cell (n - 1, n -
# 1).
# 
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1),
# (r + 1, c) and (r - 1, c) if it exists.
# 
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a -
# x| + |b - y|, where |val| denotes the absolute value of val.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
# Output: 0
# Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves
# in cells (0, 0) and (n - 1, n - 1).
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of
# 2 since:
# - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0).
# The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness
# factor.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of
# 2 since:
# - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2).
# The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
# - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2).
# The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness
# factor.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.
# 
# 
#

# @lc code=start
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]  # array DSU
    
    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, a, b, v=1):  # v for weighted DSU
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # DSU, TC: O(n^2), SC: O(n^2)
        n = len(grid)
        dq = deque()
        dis = [[-1]*n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    dq.append((i, j))
                    dis[i][j] = 0
        groups = [list(dq)]
        while dq:
            lenn = len(dq)
            for _ in range(lenn):
                i, j = dq.popleft()
                for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] == -1:
                        dis[x][y] = dis[i][j]+1
                        dq.append((x, y))
            if dq: groups.append(list(dq))
        dsu = DSU(n*n)
        for ans in range(len(groups)-1, 0, -1):
            for i, j in groups[ans]:
                for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= ans:
                        dsu.union(i*n+j, x*n+y)
                    if dsu.find(0) == dsu.find(n*n-1): return ans
        return 0
# @lc code=end

