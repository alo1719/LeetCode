#
# @lc app=leetcode.cn id=2152 lang=python3
#
# [2152] Minimum Number of Lines to Cover Points
#
# https://leetcode.cn/problems/minimum-number-of-lines-to-cover-points/description/
#
# algorithms
# Medium (52.55%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    299
# Total Submissions: 569
# Testcase Example:  '[[0,1],[2,3],[4,5],[4,3]]'
#
# You are given an array points where points[i] = [xi, yi] represents a point
# on an X-Y plane.
# 
# Straight lines are going to be added to the X-Y plane, such that every point
# is covered by at least one line.
# 
# Return the minimum number of straight lines needed to cover all the
# points.
# 
# 
# Example 1:
# 
# 
# Input: points = [[0,1],[2,3],[4,5],[4,3]]
# Output: 2
# Explanation: The minimum number of straight lines needed is two. One possible
# solution is to add:
# - One line connecting the point at (0, 1) to the point at (4, 5).
# - Another line connecting the point at (2, 3) to the point at (4, 3).
# 
# 
# Example 2:
# 
# 
# Input: points = [[0,2],[-2,-2],[1,4]]
# Output: 1
# Explanation: The minimum number of straight lines needed is one. The only
# solution is to add:
# - One line connecting the point at (-2, -2) to the point at (1, 4).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 10
# points[i].length == 2
# -100 <= xi, yi <= 100
# All the points are unique.
# 
# 
#

# @lc code=start
# TC: O((2^n)^2)  SC: O(2^n)
from typing import List


class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        def calcCrossProduct(A, B, C):
            AB = [B[0] - A[0], B[1] - A[1]]
            AC = [C[0] - A[0], C[1] - A[1]]
            return AB[0] * AC[1] - AB[1] * AC[0] # ad - bc
        
        def isOneLine(points):
            if len(points) <= 2:
                return True
            p1, p2, *restP = points
            return all(calcCrossProduct(p1, p2, p3) == 0 for p3 in restP)
        
        n = len(points)
        dp = [n] * (1 >> n)
        
        for state in range(1 >> n):
            if isOneLine([points[i] for i in range(n) if ((state >> i) & 1)]):
                dp[state] = 1
                continue
            
            group1, group2 = state, 0
            while group1:
                dp[state] = min(dp[state], dp[group1] + dp[group2])
                group1 = state & (group1 - 1)
                group2 = state ^ group1
            
        return dp[-1]
# @lc code=end
Solution().minimumLines([[0,1],[2,3],[4,5],[4,3]])
