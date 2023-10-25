#
# @lc app=leetcode id=2713 lang=python3
#
# [2713] Maximum Strictly Increasing Cells in a Matrix
#
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/description/
#
# algorithms
# Hard (21.86%)
# Likes:    214
# Dislikes: 6
# Total Accepted:    3.3K
# Total Submissions: 14.9K
# Testcase Example:  '[[3,1],[3,4]]'
#
# Given a 1-indexed m x n integer matrix mat, you can select any cell in the
# matrix as your starting cell.
# 
# From the starting cell, you can move to any other cell in the same row or
# column, but only if the value of the destination cell is strictly greater
# than the value of the current cell. You can repeat this process as many times
# as possible, moving from cell to cell until you can no longer make any
# moves.
# 
# Your task is to find the maximum number of cells that you can visit in the
# matrix by starting from some cell.
# 
# Return an integer denoting the maximum number of cells that can be
# visited.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: mat = [[3,1],[3,4]]
# Output: 2
# Explanation: The image shows how we can visit 2 cells starting from row 1,
# column 2. It can be shown that we cannot visit more than 2 cells no matter
# where we start from, so the answer is 2. 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: mat = [[1,1],[1,1]]
# Output: 1
# Explanation: Since the cells must be strictly increasing, we can only visit
# one cell in this example. 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: mat = [[3,1,6],[-9,5,7]]
# Output: 4
# Explanation: The image above shows how we can visit 4 cells starting from row
# 2, column 1. It can be shown that we cannot visit more than 4 cells no matter
# where we start from, so the answer is 4. 
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length 
# n == mat[i].length 
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# -10^5 <= mat[i][j] <= 10^5
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[mat[i][j]].append((i, j))
        dp_row = [0] * m
        dp_col = [0] * n
        for num in sorted(d.keys(), reverse=True):
            tmp = []
            for x, y in d[num]:
                tmp.append(max(dp_row[x], dp_col[y])+1)
            for i in range(len(tmp)):
                x, y = d[num][i]
                dp_row[x] = max(dp_row[x], tmp[i])
                dp_col[y] = max(dp_col[y], tmp[i])
        return max(max(dp_row), max(dp_col))
# @lc code=end
Solution().maxIncreasingCells([[5,2,9],[-6,2,-5],[-1,0,-5]])