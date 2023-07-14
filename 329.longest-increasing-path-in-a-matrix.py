#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (51.60%)
# Likes:    745
# Dislikes: 0
# Total Accepted:    93K
# Total Submissions: 180.2K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
# WeRide VOE
# TC: O(mn)  SC: O(mn)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if lens[i][j] != 1: return lens[i][j]
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0 <= i+di <= m-1 and 0 <= j+dj <= n-1 and matrix[i+di][j+dj] > matrix[i][j]:
                    lens[i][j] = max(lens[i][j], dfs(i+di, j+dj)+1)
            return lens[i][j]
        
        m, n = len(matrix), len(matrix[0])
        lens = [[1]*n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans

    # followup: print path
    def longestIncreasingPathFollowup(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if lens[i][j] != 1: return lens[i][j]
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0 <= i+di <= m-1 and 0 <= j+dj <= n-1 and matrix[i+di][j+dj] > matrix[i][j]:
                    lens[i][j] = max(lens[i][j], dfs(i+di, j+dj)+1)
            return lens[i][j]
        
        def get_path(max_len):
            nonlocal maxi, maxj
            path = [(maxi, maxj)]
            while max_len > 1:
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= maxi+di <= m-1 and 0 <= maxj+dj <= n-1 and lens[maxi+di][maxj+dj] == max_len-1:
                        max_len -= 1
                        maxi += di
                        maxj += dj
                        path.append((maxi, maxj))
            return path
        
        m, n = len(matrix), len(matrix[0])
        lens = [[1]*n for _ in range(m)]
        ans, maxi, maxj = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if tmp := dfs(i, j) > ans:
                    ans = tmp
                    maxi, maxj = i, j
        print(get_path(ans))
        return ans
# @lc code=end

