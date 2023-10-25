#
# @lc app=leetcode.cn id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#
# https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/description/
#
# algorithms
# Hard (54.25%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 7.4K
# Testcase Example:  '["A..","AAA","..."]\n3'
#
# Given a rectangular pizza represented as a rows x cols matrix containing the
# following characters: 'A' (an apple) and '.' (empty cell) and given the
# integer k. You have to cut the pizza into k pieces using k-1 cuts. 
#
# For each cut you choose the direction: vertical or horizontal, then you
# choose a cut position at the cell boundary and cut the pizza into two pieces.
# If you cut the pizza vertically, give the left part of the pizza to a person.
# If you cut the pizza horizontally, give the upper part of the pizza to a
# person. Give the last piece of pizza to the last person.
#
# Return the number of ways of cutting the pizza such that each piece contains
# at least one apple. Since the answer can be a huge number, return this modulo
# 10^9 + 7.
#
#
# Example 1:
#
#
#
#
# Input: pizza = ["A..","AAA","..."], k = 3
# Output: 3
# Explanation: The figure above shows the three ways to cut the pizza. Note
# that pieces must contain at least one apple.
#
#
# Example 2:
#
#
# Input: pizza = ["A..","AA.","..."], k = 3
# Output: 1
#
#
# Example 3:
#
#
# Input: pizza = ["A..","A..","..."], k = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza consists of characters 'A' and '.' only.
#
#

# @lc code=start
import numpy as np


class Solution:
    def ways(self, pizza, k: int) -> int:
        mod = int(1e9+7)
        rows, cols = len(pizza), len(pizza[0])
        memo = {}
        a = np.array([np.array(['A' == char for char in s], dtype=bool) for s in pizza])

        def dfs(row, col, remain):
            if (row, col, remain) in memo:
                return memo[(row, col, remain)]
            if remain <= 0:
                return 1 if True in a[row:, col:] else 0
            ttl = 0
            i, j = row, col
            while i < rows and True not in a[i, col:]: i += 1
            while i < rows-1:
                i += 1
                ttl = (ttl+dfs(i, col, remain-1))%mod
            while j < cols and True not in a[row:, j]: j += 1
            while j < cols-1:
                j += 1
                ttl = (ttl+dfs(row, j, remain-1))%mod
            memo[(row, col, remain)] = ttl
            return ttl

        return dfs(0, 0, k-1)

print(Solution().ways(["A..","AAA","..."], 3))

# @lc code=end
