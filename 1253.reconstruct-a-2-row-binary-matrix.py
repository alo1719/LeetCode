#
# @lc app=leetcode id=1253 lang=python3
#
# [1253] Reconstruct a 2-Row Binary Matrix
#
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/
#
# algorithms
# Medium (44.55%)
# Likes:    407
# Dislikes: 28
# Total Accepted:    23.2K
# Total Submissions: 52K
# Testcase Example:  '2\n1\n[1,1,1]'
#
# Given the following details of a matrix with n columns and 2 rows :
# 
# 
# The matrix is a binary matrix, which means each element in the matrix can be
# 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum
# is given as an integer array with length n.
# 
# 
# Your task is to reconstruct the matrix with upper, lower and colsum.
# 
# Return it as a 2-D integer array.
# 
# If there are more than one valid solution, any of them will be accepted.
# 
# If no valid solution exists, return an empty 2-D array.
# 
# 
# Example 1:
# 
# 
# Input: upper = 2, lower = 1, colsum = [1,1,1]
# Output: [[1,1,0],[0,0,1]]
# Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct
# answers.
# 
# 
# Example 2:
# 
# 
# Input: upper = 2, lower = 3, colsum = [2,2,1,1]
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2
# 
# 
#

# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        r1, r2 = [], []
        n = len(colsum)
        for i, c in enumerate(colsum):
            if c == 2:
                lower -= 1
                upper -= 1
                r1.append(1)
                r2.append(1)
            elif c == 1:
                if upper >= lower:
                    upper -= 1
                    r1.append(1)
                    r2.append(0)
                else:
                    lower -= 1
                    r1.append(0)
                    r2.append(1)
            else:
                r1.append(0)
                r2.append(0)
            if upper < 0 or lower < 0:
                return []
        return [r1, r2] if upper == 0 and lower == 0 else []
# @lc code=end

