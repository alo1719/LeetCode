#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Medium (39.09%)
# Likes:    11371
# Dislikes: 1408
# Total Accepted:    1.3M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
#
#
# Follow up:
#
#
# Try to come up with as many solutions as you can. There are at least three
# different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Reverse the whole list, like this:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # 2. Use queue
        # 3. pop and insert k times


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)

# @lc code=end
