#
# @lc app=leetcode.cn id=2750 lang=python3
#
# [2750] Ways to Split Array Into Good Subarrays
#
# https://leetcode.cn/problems/ways-to-split-array-into-good-subarrays/description/
#
# algorithms
# Medium (38.93%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 9.6K
# Testcase Example:  '[0,1,0,0,1]'
#
# You are given a binary array nums.
# 
# A subarray of an array is good if it contains exactly one element with the
# value 1.
# 
# Return an integer denoting the number of ways to split the array nums into
# good subarrays. As the number may be too large, return it modulo 10^9 + 7.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [0,1,0,0,1]
# Output: 3
# Explanation: There are 3 ways to split nums into good subarrays:
# - [0,1] [0,0,1]
# - [0,1,0] [0,1]
# - [0,1,0,0] [1]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0]
# Output: 1
# Explanation: There is 1 way to split nums into good subarrays:
# - [0,1,0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        @cache
        def f(i, ok):
            if i == n: return int(ok)
            if ok and nums[i] == 0: return f(i+1, False)+f(i+1, True) % MOD
            if ok and nums[i] == 1: return f(i+1, True) % MOD
            if not ok: return f(i+1, nums[i] == 1) % MOD
            
        n = len(nums)
        MOD = 10**9+7
        return f(0, False)
# @lc code=end

