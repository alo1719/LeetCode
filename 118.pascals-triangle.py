#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (68.58%)
# Likes:    7927
# Dislikes: 266
# Total Accepted:    1M
# Total Submissions: 1.5M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= numRows <= 30
#
#
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[None for _ in range(numRows)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangle[i][j] = 1
                else:
                    triangle[i][j] = triangle[i - 1][j - 1] + \
                        triangle[i - 1][j]
        return [row[:i + 1] for i, row in enumerate(triangle)]


a = Solution().generate(5)
print(a)

# @lc code=end
