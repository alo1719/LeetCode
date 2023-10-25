#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.cn/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (54.88%)
# Likes:    3316
# Dislikes: 0
# Total Accepted:    767.3K
# Total Submissions: 1.4M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp: n^2
        # greedy + binary search: nlogn
        # g[i]: the smallest ending number of all increasing subsequences with length i
        # swap the value and state
        # g is increasing, so we can use binary search
        g = []
        for x in nums:
            j = bisect.bisect_left(g, x)  # bisect_right if accept equal
            if j == len(g): g.append(x)
            else: g[j] = x
        return len(g)
# @lc code=end

