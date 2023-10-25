#
# @lc app=leetcode.cn id=2815 lang=python3
#
# [2815] Max Pair Sum in an Array
#
# https://leetcode.cn/problems/max-pair-sum-in-an-array/description/
#
# algorithms
# Easy (68.61%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 8.3K
# Testcase Example:  '[51,71,17,24,42]'
#
# You are given a 0-indexed integer array nums. You have to find the maximum
# sum of a pair of numbers from nums such that the maximum digit in both
# numbers are equal.
# 
# Return the maximum sum or -1 if no such pair exists.
# 
# 
# Example 1:
# 
# 
# Input: nums = [51,71,17,24,42]
# Output: 88
# Explanation: 
# For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a
# pair sum of 71 + 17 = 88. 
# For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a
# pair sum of 24 + 42 = 66.
# It can be shown that there are no other pairs with equal maximum digits, so
# the answer is 88.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: No pair exists in nums with equal maximum digits.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
# TC: O(nlogU)  SC: O(1)
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        max_val = [-inf]*10
        for x in nums:
            maxx = max(int(ch) for ch in str(x))
            ans = max(ans, max_val[maxx]+x)
            max_val[maxx] = max(max_val[maxx], x)
        return ans
# @lc code=end

