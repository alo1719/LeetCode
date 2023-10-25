#
# @lc app=leetcode.cn id=2552 lang=python3
#
# [2552] Count Increasing Quadruplets
#
# https://leetcode.cn/problems/count-increasing-quadruplets/description/
#
# algorithms
# Hard (41.67%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 8.3K
# Testcase Example:  '[1,3,2,4,5]'
#
# Given a 0-indexed integer array nums of size n containing all numbers from 1
# to n, return the number of increasing quadruplets.
# 
# A quadruplet (i, j, k, l) is increasing if:
# 
# 
# 0 <= i < j < k < l < n, and
# nums[i] < nums[k] < nums[j] < nums[l].
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,2,4,5]
# Output: 2
# Explanation: 
# - When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
# - When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] <
# nums[l]. 
# There are no other quadruplets, so we return 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4]
# Output: 0
# Explanation: There exists only one quadruplet with i = 0, j = 1, k = 2, l =
# 3, but since nums[j] < nums[k], we return 0.
# 
# 
# 
# Constraints:
# 
# 
# 4 <= nums.length <= 4000
# 1 <= nums[i] <= nums.length
# All the integers of nums are unique. nums is a permutation.
# 
# 
#

# @lc code=start
# TC: O(n^2)  SC: O(n^2)
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # enumerate j and k
        # then find how many numbers on the right of k is larger than nums[j]
        # and how many numbers on the left of j is smaller than nums[k]
        # the numbers and be pre-calculated
        # greater[k][x]: on the right of k, how many numbers are greater than x
        # less[j][x]: on the left of j, how many numbers are smaller than x
        n = len(nums)
        greater = [[0]*(n+1) for _ in range(n)]
        for k in range(n-2, -1, -1):
            greater[k] = greater[k+1][:]
            for x in range(1, nums[k+1]):
                greater[k][x] += 1
        less = [[0]*(n+1) for _ in range(n)]
        ans = 0
        for j in range(1, n-1):
            less[j] = less[j-1][:]
            for x in range(nums[j-1]+1, n+1):
                less[j][x] += 1
            for k in range(j+1, n-1):
                if nums[j] > nums[k]:
                    ans += less[j][nums[k]]*greater[k][nums[j]]
        return ans
# @lc code=end

