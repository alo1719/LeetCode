#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.cn/problems/find-peak-element/description/
#
# algorithms
# Medium (49.47%)
# Likes:    900
# Dislikes: 0
# Total Accepted:    262.6K
# Total Submissions: 530.8K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
# 
# Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of the
# peaks.
# 
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the
# array.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# 
# 
#

# @lc code=start
from curses.ascii import SO
from typing import List

# TC: O(logn)  SC: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return n-1
        # find ↑↓
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left


Solution().findPeakElement([1, 2, 3, 1])
Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
# @lc code=end

