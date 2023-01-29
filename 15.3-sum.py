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
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dict = {}
        for i in range(n):
            dict.setdefault(nums[i], [])
            dict[nums[i]].append(i)
        ans = []
        ans_set = set()
        for i in range(n):
            for j in range(i + 1, n):
                goal = - nums[i] - nums[j]
                if goal in dict and dict[goal][-1] > j:
                    tmp_ans = sorted([nums[i], nums[j], goal])
                    if str(tmp_ans) not in ans_set:
                        ans.append(tmp_ans)
                        ans_set.add(str(tmp_ans))
        return ans
# @lc code=end

