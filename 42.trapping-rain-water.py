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
# TC: O(n)  SC: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. two pointers
        # TC: O(n)  SC: O(1)
        n = len(height)
        left, right, pre_max, suf_max, ans = 0, n-1, 0, 0, 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max-height[left]
                left += 1
            else:
                ans += suf_max-height[right]
                right -= 1
        return ans
        # 2. monotonic stack
        # TC: O(n)  SC: O(n)
        n, stk, ans = len(height), [], 0  # stack stores position accroding to its value monotonically
        for i in range(n):
            now_height = height[i]
            while stk and now_height >= height[stk[-1]]: # increasing, pop and calculate
                popped_pos = stk.pop()
                if not stk: break
                # the usage of monotonic stack is to know the closest pos with greater/less value
                # but for this question it's not the closest greater value pos for **current node**,
                # but for the **popped** node because trapped water needs to be accumulated
                # step by step.
                left = stk[-1] 
                trapped_height = min(height[left], now_height)-height[popped_pos]
                trapped_length = i-left-1
                ans += trapped_height*trapped_length
            stk.append(i)  # decreasing, append
        return ans
# @lc code=end

