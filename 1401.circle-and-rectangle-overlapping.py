#
# @lc app=leetcode.cn id=1401 lang=python3
#
# [1401] Circle and Rectangle Overlapping
#
# https://leetcode.cn/problems/circle-and-rectangle-overlapping/description/
#
# algorithms
# Medium (51.76%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 35.2K
# Testcase Example:  '1\n0\n0\n1\n-1\n3\n1'
#
# You are given a circle represented as (radius, xCenter, yCenter) and an
# axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are
# the coordinates of the bottom-left corner, and (x2, y2) are the coordinates
# of the top-right corner of the rectangle.
# 
# Return true if the circle and rectangle are overlapped otherwise return
# false. In other words, check if there is any point (xi, yi) that belongs to
# the circle and the rectangle at the same time.
# 
# 
# Example 1:
# 
# 
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# Output: true
# Explanation: Circle and rectangle share the point (1,0).
# 
# 
# Example 2:
# 
# 
# Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= radius <= 2000
# -10^4 <= xCenter, yCenter <= 10^4
# -10^4 <= x1 < x2 <= 10^4
# -10^4 <= y1 < y2 <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        #  x3, y3 ---------- x2, y2
        #     |                 |
        #     |                 |
        #  x1, y1 ---------- x4, y4
        x3, y3 = x1, y2
        x4, y4 = x2, y1
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2: return True
        if x1 <= xCenter <= x2 and (y1-radius <= yCenter <= y2+radius): return True
        if y1 <= yCenter <= y2 and (x1-radius <= xCenter <= x2+radius): return True
        return min((x1-xCenter)**2+(y1-yCenter)**2,\
                   (x2-xCenter)**2+(y2-yCenter)**2,\
                   (x3-xCenter)**2+(y3-yCenter)**2,\
                   (x4-xCenter)**2+(y4-yCenter)**2\
                  ) <= radius**2
# @lc code=end

