#
# @lc app=leetcode id=2711 lang=python3
#
# [2711] Difference of Number of Distinct Values on Diagonals
#
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/description/
#
# algorithms
# Medium (72.52%)
# Likes:    66
# Dislikes: 134
# Total Accepted:    13.7K
# Total Submissions: 18.9K
# Testcase Example:  '[[1,2,3],[3,1,5],[3,2,1]]'
#
# Given a 0-indexed 2D grid of size m x n, you should find the matrix answer of
# size m x n.
# 
# The value of each cell (r, c) of the matrix answer is calculated in the
# following way:
# 
# 
# Let topLeft[r][c] be the number of distinct values in the top-left diagonal
# of the cell (r, c) in the matrix grid.
# Let bottomRight[r][c] be the number of distinct values in the bottom-right
# diagonal of the cell (r, c) in the matrix grid.
# 
# 
# Then answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|.
# 
# Return the matrix answer.
# 
# A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right
# direction until reaching the matrix's end.
# 
# A cell (r1, c1) belongs to the top-left diagonal of the cell (r, c), if both
# belong to the same diagonal and r1 < r. Similarly is defined bottom-right
# diagonal.
# 
# 
# Example 1:
# 
# 
# 
# Input: grid = [[1,2,3],[3,1,5],[3,2,1]]
# Output: [[1,1,0],[1,0,1],[0,1,1]]
# Explanation: The 1^st diagram denotes the initial grid. 
# The 2^nd diagram denotes a grid for cell (0,0), where blue-colored cells are
# cells on its bottom-right diagonal.
# The 3^rd diagram denotes a grid for cell (1,2), where red-colored cells are
# cells on its top-left diagonal.
# The 4^th diagram denotes a grid for cell (1,1), where blue-colored cells are
# cells on its bottom-right diagonal and red-colored cells are cells on its
# top-left diagonal.
# - The cell (0,0) contains [1,1] on its bottom-right diagonal and [] on its
# top-left diagonal. The answer is |1 - 0| = 1.
# - The cell (1,2) contains [] on its bottom-right diagonal and [2] on its
# top-left diagonal. The answer is |0 - 1| = 1.
# - The cell (1,1) contains [1] on its bottom-right diagonal and [1] on its
# top-left diagonal. The answer is |1 - 1| = 0.
# The answers of other cells are similarly calculated.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1]]
# Output: [[0]]
# Explanation: - The cell (0,0) contains [] on its bottom-right diagonal and []
# on its top-left diagonal. The answer is |0 - 0| = 0.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n, grid[i][j] <= 50
# 
# 
#

# @lc code=start
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        left = [[0]*n for _ in range(m)]
        right = [[0]*n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            j = 0
            sett = set()
            while i < m and j < n:
                left[i][j] = len(sett)
                sett.add(grid[i][j])
                i += 1
                j += 1
        for j in range(1, n):
            i = 0
            sett = set()
            while i < m and j < n:
                left[i][j] = len(sett)
                sett.add(grid[i][j])
                i += 1
                j += 1
        for i in range(m):
            j = n-1
            sett = set()
            while i >= 0 and j >= 0:
                right[i][j] = len(sett)
                sett.add(grid[i][j])
                i -= 1
                j -= 1
        for j in range(n-1):
            i = m-1
            sett = set()
            while i >= 0 and j >= 0:
                right[i][j] = len(sett)
                sett.add(grid[i][j])
                i -= 1
                j -= 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = abs(left[i][j]-right[i][j])
        return ans
# @lc code=end

