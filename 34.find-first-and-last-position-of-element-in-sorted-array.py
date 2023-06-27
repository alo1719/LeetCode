#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.38%)
# Likes:    2245
# Dislikes: 0
# Total Accepted:    765.2K
# Total Submissions: 1.8M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        leftmost = left if left < n and nums[left] == target else -1
        left, right = 0, n-1
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid
        rightmost = left if left < n and nums[left] == target else -1
        return [leftmost, rightmost]
# @lc code=end

