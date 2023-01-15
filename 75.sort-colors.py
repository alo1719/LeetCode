#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.cn/problems/sort-colors/description/
#
# algorithms
# Medium (60.09%)
# Likes:    1419
# Dislikes: 0
# Total Accepted:    454.7K
# Total Submissions: 756.6K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
# Example 1:
#
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
#
# Example 2:
#
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
#
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2  2  2  1  1  0
        # p0             p2
        # i
        # 0  2  2  1  1  2
        #    p0       p2 
        #    i
        # 0  1  1  2  2  2
        #    p0 p2 
        #          i
        # 2  0  1
        # p0    p2
        # i
        # 1  0  2
        # p0 p2
        #    i
        n = len(nums)
        p0 = 0 # the start of 1
        p2 = n - 1 # the end of 1
        i = 0 
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1


Solution().sortColors([2, 0, 2, 1, 1, 0])
Solution().sortColors([2, 0, 1])
# @lc code=end
