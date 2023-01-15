#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (62.32%)
# Likes:    4035
# Dislikes: 0
# Total Accepted:    622.3K
# Total Submissions: 998.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stk = []
        ans = 0
        for i in range(n):
            now_height = height[i]
            if not stk or height[stk[-1]] >= now_height:
                stk.append(i)
            if stk and now_height > height[stk[-1]]:
                while stk and height[stk[-1]] <= now_height:
                    now = stk.pop()
                    if not stk: break
                    left = stk[-1]
                    ans += (min(height[left], now_height) - height[now]) * (i - left - 1)
                stk.append(i)
        return ans
# @lc code=end

