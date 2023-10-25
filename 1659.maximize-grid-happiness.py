#
# @lc app=leetcode id=1659 lang=python3
#
# [1659] Maximize Grid Happiness
#
# https://leetcode.com/problems/maximize-grid-happiness/description/
#
# algorithms
# Hard (38.95%)
# Likes:    294
# Dislikes: 51
# Total Accepted:    4.6K
# Total Submissions: 11.7K
# Testcase Example:  '2\n3\n1\n2'
#
# You are given four integers, m, n, introvertsCount, and extrovertsCount. You
# have an m x n grid, and there are two types of people: introverts and
# extroverts. There are introvertsCount introverts and extrovertsCount
# extroverts.
# 
# You should decide how many people you want to live in the grid and assign
# each of them one grid cell. Note that you do not have to have all the people
# living in the grid.
# 
# The happiness of each person is calculated as follows:
# 
# 
# Introverts start with 120 happiness and lose 30 happiness for each neighbor
# (introvert or extrovert).
# Extroverts start with 40 happiness and gain 20 happiness for each neighbor
# (introvert or extrovert).
# 
# 
# Neighbors live in the directly adjacent cells north, east, south, and west of
# a person's cell.
# 
# The grid happiness is the sum of each person's happiness. Return the maximum
# possible grid happiness.
# 
# 
# Example 1:
# 
# 
# Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# Output: 240
# Explanation: Assume the grid is 1-indexed with coordinates (row, column).
# We can put the introvert in cell (1,1) and put the extroverts in cells (1,3)
# and (2,3).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0
# neighbors) = 120
# - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1
# neighbor) = 60
# - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1
# neighbor) = 60
# The grid happiness is 120 + 60 + 60 = 240.
# The above figure shows the grid in this example with each person's happiness.
# The introvert stays in the light green cell while the extroverts live on the
# light purple cells.
# 
# 
# Example 2:
# 
# 
# Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# Output: 260
# Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at
# (2,1).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1
# neighbor) = 90
# - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2
# neighbors) = 80
# - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1
# neighbor) = 90
# The grid happiness is 90 + 80 + 90 = 260.
# 
# 
# Example 3:
# 
# 
# Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# Output: 240
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 5
# 0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
# 
# 
#

# @lc code=start
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:
        @cache
        def calc(x: int, y: int) -> int:
            if x == 0 or y == 0: return 0
            if x == 1 and y == 1: return -60
            if x == 2 and y == 2: return 40
            return -10
        
        n3 = 3**n
        mask_span = {}
        truncate = {}

        highest = n3//3
        for mask in range(n3):
            mask_tmp = mask
            bits = list()
            for i in range(n):
                bits.append(mask_tmp%3)
                mask_tmp //= 3
            mask_span[mask] = bits[::-1]
            truncate[mask] = [
                mask%highest*3,
                mask%highest*3+1,
                mask%highest*3+2,
            ]
        
        @cache
        def dfs(pos: int, borderline: int, nx: int, wx: int):
            if pos == m*n or nx+wx == 0: return 0
            
            y = pos%n
            put0, put1, put2 = dfs(pos+1, truncate[borderline][0], nx, wx), 0, 0
            if nx > 0:
                put1 = 120+calc(1, mask_span[borderline][0])+(0 if y == 0 else calc(1, mask_span[borderline][-1]))+dfs(pos+1, truncate[borderline][1], nx-1, wx)
            if wx > 0:
                put2 = 40+calc(2, mask_span[borderline][0])+(0 if y == 0 else calc(2, mask_span[borderline][-1]))+dfs(pos+1, truncate[borderline][2], nx, wx-1)
            return max(put0, put1, put2)

        return dfs(0, 0, nx, wx)
# @lc code=end

