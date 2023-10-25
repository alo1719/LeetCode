#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.cn/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (47.70%)
# Likes:    408
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 113.6K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an integer array nums and an integer k, return the number of non-empty
# subarrays that have a sum divisible by k.
# 
# A subarray is a contiguous part of an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# Example 2:
# 
# 
# Input: nums = [5], k = 9
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4
# 
# 
#

# @lc code=start
# Use the property of modulo
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod_array = [0]*n
        sum = 0
        for i in range(n):
            sum += nums[i]
            mod_array[i] = sum%k
        mod_map = {0: 1}
        ans = 0
        for i in range(n):
            if mod_array[i] in mod_map:
                ans += mod_map[mod_array[i]]
            if mod_array[i] not in mod_map:
                mod_map[mod_array[i]] = 1
            else:
                mod_map[mod_array[i]] += 1
        return ans
# @lc code=end
