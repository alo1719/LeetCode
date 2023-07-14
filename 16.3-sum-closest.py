#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.61%)
# Likes:    9428
# Dislikes: 487
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
# TC: O(n^2)  SC: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = inf
        ans = 0
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == target: return target
                diff = abs(nums[i]+nums[j]+nums[k]-target)
                if diff < min_diff:
                    min_diff = diff
                    ans = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return ans
# @lc code=end

