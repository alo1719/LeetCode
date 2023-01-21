#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.cn/problems/number-of-islands/description/
#
# algorithms
# Medium (58.77%)
# Likes:    1964
# Dislikes: 0
# Total Accepted:    574.5K
# Total Submissions: 977.6K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            nonlocal n, m
            if  i >= n or i < 0 or j >= m or j < 0 or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans
# @lc code=end

