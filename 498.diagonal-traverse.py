#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (57.87%)
# Likes:    2560
# Dislikes: 575
# Total Accepted:    224.3K
# Total Submissions: 387.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix mat, return an array of all the elements of the array
# in a diagonal order.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        res = []
        for _ in range(m*n):
            res.append(mat[i][j])
            if (i+j)%2 == 0:
                if j == n-1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return res
# @lc code=end

