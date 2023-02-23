#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (65.86%)
# Likes:    1153
# Dislikes: 0
# Total Accepted:    256.2K
# Total Submissions: 388.9K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in
# nums.
# 
# 
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# 
# 
# 
# Follow up: Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.
# 
#

# @lc code=start
# Snowflake VOE
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n, ans = len(nums), []
        for i in range(n):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                # cannot reverse, because first set left then set right
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
# @lc code=end

