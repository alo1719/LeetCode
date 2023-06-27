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

# TC: O(n^2)  SC: O(n^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*(numRows+1) for _ in range(numRows)]
        ans[0][1] = 1
        for i in range(1, numRows):
            for j in range(1, i+2):
                ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        return [row[1:i+2] for i, row in enumerate(ans)]

a = Solution().generate(5)
print(a)

# @lc code=end
