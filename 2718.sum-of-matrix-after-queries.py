#
# @lc app=leetcode id=2718 lang=python3
#
# [2718] Sum of Matrix After Queries
#
# https://leetcode.com/problems/sum-of-matrix-after-queries/description/
#
# algorithms
# Medium (25.98%)
# Likes:    363
# Dislikes: 16
# Total Accepted:    10.8K
# Total Submissions: 41.7K
# Testcase Example:  '3\n[[0,0,1],[1,2,2],[0,2,3],[1,0,4]]'
#
# You are given an integer n and a 0-indexed 2D array queries where queries[i]
# = [typei, indexi, vali].
# 
# Initially, there is a 0-indexed n x n matrix filled with 0's. For each query,
# you must apply one of the following changes:
# 
# 
# if typei == 0, set the values in the row with indexi to vali, overwriting any
# previous values.
# if typei == 1, set the values in the column with indexi to vali, overwriting
# any previous values.
# 
# 
# Return the sum of integers in the matrix after all queries are applied.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
# Output: 23
# Explanation: The image above describes the matrix after each query. The sum
# of the matrix after all queries are applied is 23. 
# 
# 
# Example 2:
# 
# 
# Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
# Output: 17
# Explanation: The image above describes the matrix after each query. The sum
# of the matrix after all queries are applied is 17.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 1 <= queries.length <= 5 * 10^4
# queries[i].length == 3
# 0 <= typei <= 1
# 0 <= indexi < n
# 0 <= vali <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row = set()
        col = set()
        ans = 0
        for tp, index, val in reversed(queries):
            if tp == 0 and index not in row:
                row.add(index)
                ans += (n-len(col))*val
            if tp == 1 and index not in col:
                col.add(index)
                ans += (n-len(row))*val
        return ans
# @lc code=end

