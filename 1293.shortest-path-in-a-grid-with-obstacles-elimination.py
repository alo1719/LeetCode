#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (38.20%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 55.8K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# You are given an m x n integer matrix grid where each cell is either 0
# (empty) or 1 (obstacle). You can move up, down, left, or right from and to an
# empty cell in one step.
# 
# Return the minimum number of steps to walk from the upper left corner (0, 0)
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most
# k obstacles. If it is not possible to find such walk return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a
# walk.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
# 
# 
#

# @lc code=start
from collections import deque

# WeRide VOE
# TC: O(m*n*k)  SC: O(m*n*k)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # followup: cut branches
        if k >= m+n-3: return m+n-2
        visited = set()
        visited.add((0, 0, k))
        dq = deque()
        dq.append((0, 0, k))
        
        step = 0
        while dq:
            step += 1
            count = len(dq)
            for _ in range(count):
                x, y, left = dq.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, left) not in visited:
                            if nx == m-1 and ny == n-1:
                                return step
                            visited.add((nx, ny, left))
                            dq.append((nx, ny, left))
                        elif grid[nx][ny] == 1 and left > 0 and (nx, ny, left-1) not in visited:
                            visited.add((nx, ny, left-1))
                            dq.append((nx, ny, left-1))
        return -1
# @lc code=end

