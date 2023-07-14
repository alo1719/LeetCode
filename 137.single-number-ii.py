#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (58.74%)
# Likes:    5757
# Dislikes: 555
# Total Accepted:    422K
# Total Submissions: 716.6K
# Testcase Example:  '[2,2,3,2]'
#
# Given an integer array nums where every element appears three times except
# for one, which appears exactly once. Find the single element and return it.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# 
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each element in nums appears exactly three times except for one element which
# appears once.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # think about each bit
        # if the bit can be divided by 3, then the single number's bit is 0, otherwise 1
        n = len(nums)
        ans = 0
        for digit in range(32):
            acc = 0
            for i in range(n):
                acc += (nums[i]>>digit)&1
            if acc%3:
                if digit == 31: ans -= 1<<digit
                else: ans += 1<<digit
        return ans
# @lc code=end

