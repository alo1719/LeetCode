#
# @lc app=leetcode.cn id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#
# https://leetcode.cn/problems/detect-cycles-in-2d-grid/description/
#
# algorithms
# Medium (39.63%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 15.7K
# Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# Given a 2D array of characters grid of size m x n, you need to find if there
# exists any cycle consisting of the same value in grid.
# 
# A cycle is a path of length 4 or more in the grid that starts and ends at the
# same cell. From a given cell, you can move to one of the cells adjacent to it
# - in one of the four directions (up, down, left, or right), if it has the
# same value of the current cell.
# 
# Also, you cannot move to the cell that you visited in your last move. For
# example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2)
# we visited (1, 1) which was the last visited cell.
# 
# Return true if any cycle of the same value exists in grid, otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the
# image below:
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Do not need to backtrack!
        def dfs(lasti, lastj, i, j):
            nonlocal ok
            if ok:
                return
            if visited[i][j]:
                ok = True
                return
            visited[i][j] = 1
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (i+dx, j+dy) != (lasti, lastj):
                    newi = i+dx
                    newj = j+dy
                    if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == grid[i][j]:
                        dfs(i, j, newi, newj)
        
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ok = False
                if not visited[i][j]:
                    dfs(-1, -1, i, j)
                if ok: return True
        return False
# @lc code=end

