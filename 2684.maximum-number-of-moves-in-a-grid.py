#
# @lc app=leetcode id=2684 lang=python3
#
# [2684] Maximum Number of Moves in a Grid
#
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
#
# algorithms
# Medium (44.52%)
# Likes:    209
# Dislikes: 3
# Total Accepted:    12.2K
# Total Submissions: 27.4K
# Testcase Example:  '[[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]'
#
# You are given a 0-indexed m x n matrix grid consisting of positive integers.
# 
# You can start at any cell in the first column of the matrix, and traverse the
# grid in the following way:
# 
# 
# From a cell (row, col), you can move to any of the cells: (row - 1, col + 1),
# (row, col + 1) and (row + 1, col + 1) such that the value of the cell you
# move to, should be strictly bigger than the value of the current cell.
# 
# 
# Return the maximum number of moves that you can perform.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# Output: 3
# Explanation: We can start at the cell (0, 0) and make the following moves:
# - (0, 0) -> (0, 1).
# - (0, 1) -> (1, 2).
# - (1, 2) -> (2, 3).
# It can be shown that it is the maximum number of moves that can be made.
# 
# Example 2:
# 
# 
# 
# Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
# Output: 0
# Explanation: Starting from any cell in the first column we cannot perform any
# moves.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 10^5
# 1 <= grid[i][j] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            for dx, dy in [(-1,1),(0,1),(1,1)]:
                newx = i+dx
                newy = j+dy
                if 0 <= newx < m and 0 <= newy < n and grid[i][j] < grid[newx][newy]:
                    if ans[newx][newy] == 0:
                        dfs(newx, newy)
                    ans[i][j] = max(ans[i][j], ans[newx][newy]+1)
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            dfs(i, 0)
        return max(max(ans))
# @lc code=end

