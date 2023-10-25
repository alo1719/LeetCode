#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (44.47%)
# Likes:    3958
# Dislikes: 167
# Total Accepted:    265.3K
# Total Submissions: 596.6K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
# 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
# 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they
# are different and they share an edge or a corner).
# 
# 
# The length of a clear path is the number of visited cells of this path.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1],[1,0]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# 
# 
#

# @lc code=start
from curses.ascii import SO
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        grid[0][0] = 1
        q = [(0, 0, 1)]
        for i, j, d in q:
            if i == len(grid)-1 and j == len(grid)-1: return d
            for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 0:
                    # remove visited node
                    grid[x][y] = 1
                    q.append((x, y, d+1))
                    # print(q)
        return -1

Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]])
print('-------------------------------')
Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
# @lc code=end

