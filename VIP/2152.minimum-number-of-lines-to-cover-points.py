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

from functools import cache
from typing import List

# TC: O(n^3*2^n)  SC: O(2^n)
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:        
        @cache
        def one_line(A, B, C):
            AB = [points[B][0]-points[A][0], points[B][1]-points[A][1]]
            AC = [points[C][0]-points[A][0], points[C][1]-points[A][1]]
            return AB[0]*AC[1]-AB[1]*AC[0] == 0  # ad - bc
        
        @cache
        def f(mask):
            if mask == (1<<n)-1: return 0
            ans = float('inf')
            for i in range(n):
                if (mask>>i)&1 == 0:
                    for j in range(n):
                        if i == j or mask>>j&1 == 1: continue
                        now = mask|(1<<i)|(1<<j)
                        for k in range(n):
                            if (1<<k)&now == 0 and one_line(i, j, k):
                                now |= 1<<k
                        ans = min(ans, f(now)+1)
            return ans

        n = len(points)
        return f(0)
        
# @lc code=end
print(Solution().minimumLines([[0,1],[2,3],[4,5],[4,3]]))  # 2
print(Solution().minimumLines([[0,2],[-2,-2],[1,4]]))  # 1
