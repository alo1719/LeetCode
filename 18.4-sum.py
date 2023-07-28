#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (35.78%)
# Likes:    9793
# Dislikes: 1167
# Total Accepted:    770.3K
# Total Submissions: 2.2M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
# TC: O(n^3)  SC: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                left, right = j+1, n-1
                while left < right:
                    if nums[i]+nums[j]+nums[left]+nums[right] == target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        while left < n and nums[left] == nums[left-1]: left += 1
                        right -= 1
                        while right > 0 and nums[right] == nums[right+1]: right -= 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return ans
# @lc code=end

