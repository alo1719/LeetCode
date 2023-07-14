#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.cn/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (64.44%)
# Likes:    2060
# Dislikes: 0
# Total Accepted:    299.2K
# Total Submissions: 464.5K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
# 
# There is only one repeated number in nums, return this repeated number.
# 
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,1,3,4,2]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
# 
# 
# 
# Follow up:
# 
# 
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow, fast = nums[0], nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
# @lc code=end

