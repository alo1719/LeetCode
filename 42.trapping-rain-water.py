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
        n, stack, ans = len(height), [], 0 # stack stores position accroding to its value monotonically
        for i in range(n):
            now_height = height[i]
            if not stack or now_height <= height[stack[-1]]:
                stack.append(i)
            if stack and now_height >= height[stack[-1]]: # not monotonically decreasing, pop
                while stack and now_height >= height[stack[-1]]:
                    popped_pos = stack.pop()
                    if not stack: break
                    # the usage of monotonic stack
                    # but for this question it's not the closest bigger pos for **current node**,
                    # but for the **popped** node because trapped water needs to be accumulated
                    # step by step.
                    closest_bigger_pos = stack[-1] 
                    trapped_height = min(height[closest_bigger_pos], now_height) - height[popped_pos]
                    trapped_length = i - closest_bigger_pos - 1
                    ans += trapped_height * trapped_length
                stack.append(i)
        return ans
# @lc code=end

