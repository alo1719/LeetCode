#
# @lc app=leetcode id=2500 lang=python3
#
# [2500] Delete Greatest Value in Each Row
#
# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
#
# algorithms
# Easy (79.17%)
# Likes:    473
# Dislikes: 24
# Total Accepted:    38.3K
# Total Submissions: 48.4K
# Testcase Example:  '[[1,2,4],[3,3,1]]'
#
# You are given an m x n matrix grid consisting of positive integers.
# 
# Perform the following operation until grid becomes empty:
# 
# 
# Delete the element with the greatest value from each row. If multiple such
# elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# 
# 
# Note that the number of columns decreases by one after each operation.
# 
# Return the answer after performing the operations described above.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,2,4],[3,3,1]]
# Output: 8
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 4 from the first row and 3 from the
# second row (notice that, there are two cells with value 3 and we can remove
# any of them). We add 4 to the answer.
# - In the second operation, we remove 2 from the first row and 3 from the
# second row. We add 3 to the answer.
# - In the third operation, we remove 1 from the first row and 1 from the
# second row. We add 1 to the answer.
# The final answer = 4 + 3 + 1 = 8.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[10]]
# Output: 10
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 10 from the first row. We add 10 to the
# answer.
# The final answer = 10.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 100
# 
# 
#

# @lc code=start
# TC: O(mnlogn)  SC: O(1)
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid:
            row.sort(reverse=True)
        ans = 0
        for j in range(n):
            ans += max(grid[i][j] for i in range(m))
        return ans
# @lc code=end

