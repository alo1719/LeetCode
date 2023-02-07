#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (41.60%)
# Likes:    998
# Dislikes: 0
# Total Accepted:    164.7K
# Total Submissions: 395.8K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array nums, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order.
# 
# Return the shortest such subarray and output its length.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4]
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: nums = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: Can you solve it in O(n) time complexity?
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n-1, 0
        # while True:
        #     if left == right: return 0
        #     min_value = min(nums[left+1:right+1])
        #     max_value = max(nums[left:right])
        #     if min_value >= nums[left]:
        #         left += 1
        #         continue
        #     elif max_value <= nums[right]:
        #         right -= 1
        #         continue
        #     else: return right-left+1
        max_value = -float("inf")
        for i in range(n):
            max_value = max(max_value, nums[i])
            if nums[i] < max_value:
                right = i
        min_value = float("inf")
        for i in range(n-1, -1, -1):
            min_value = min(min_value, nums[i])
            if nums[i] > min_value:
                left = i
        return 0 if left >= right else right-left+1
# @lc code=end

