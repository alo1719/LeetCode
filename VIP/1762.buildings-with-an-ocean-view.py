#
# @lc app=leetcode.cn id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#
# https://leetcode.cn/problems/buildings-with-an-ocean-view/description/
#
# algorithms
# Medium (71.39%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 3.6K
# Testcase Example:  '[4,2,3,1]'
#
# There are n buildings in a line. You are given an integer array heights of
# size n that represents the heights of the buildings in the line.
# 
# The ocean is to the right of the buildings. A building has an ocean view if
# the building can see the ocean without obstructions. Formally, a building has
# an ocean view if all the buildings to its right have a smaller height.
# 
# Return a list of indices (0-indexed) of buildings that have an ocean view,
# sorted in increasing order.
# 
# 
# Example 1:
# 
# 
# Input: heights = [4,2,3,1]
# Output: [0,2,3]
# Explanation: Building 1 (0-indexed) does not have an ocean view because
# building 2 is taller.
# 
# 
# Example 2:
# 
# 
# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]
# Explanation: All the buildings have an ocean view.
# 
# 
# Example 3:
# 
# 
# Input: heights = [1,3,2,4]
# Output: [3]
# Explanation: Only building 3 has an ocean view.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^9
# 
# 
#

# @lc code=start
from typing import List

# TC: O(n)  SC: O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxx = 0
        ans = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxx:
                ans.append(i)
                maxx = heights[i]
        return ans[::-1]
# @lc code=end
