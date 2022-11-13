#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (57.14%)
# Likes:    811
# Dislikes: 0
# Total Accepted:    160.5K
# Total Submissions: 280.9K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    ans = max(ans, dp[i + 1][j + 1])
        return ans
# @lc code=end

