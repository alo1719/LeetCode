#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (61.24%)
# Likes:    11128
# Dislikes: 275
# Total Accepted:    1.9M
# Total Submissions: 3.1M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you minimize the total number of operations done?
#

# @lc code=start
# TC: O(n)  SC: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
# @lc code=end
