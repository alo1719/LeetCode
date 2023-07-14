#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (36.61%)
# Likes:    5560
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 3.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
# TC: O(n^2)  SC: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]: continue
            j, k = i+1, n-1
            while j < k:
                y, z = nums[j], nums[k]
                if x+y+z == 0:
                    ans.append([x, y, z])
                    while j < k and nums[j] == y:
                        j += 1
                    while j < k and nums[k] == z:
                        k -= 1
                elif x+y+z < 0:
                    j += 1
                else:
                    k -= 1
        return ans
# @lc code=end
