#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (49.97%)
# Likes:    25177
# Dislikes: 1157
# Total Accepted:    2.7M
# Total Submissions: 5.5M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#

# @lc code=start
from typing import List

# TC: O(n)  SC: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, ans = len(nums), -inf
        dp = 0
        # dp[i] = max(nums[i], nums[i]+dp[i-1])
        for i in range(n):
            dp = max(nums[i], nums[i]+dp)
            ans = max(ans, dp)
        return ans


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
#                       0   1   0  4   3  5  6   1  5
# @lc code=end
