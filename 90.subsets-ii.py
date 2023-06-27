#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.cn/problems/subsets-ii/description/
#
# algorithms
# Medium (63.69%)
# Likes:    1047
# Dislikes: 0
# Total Accepted:    279.7K
# Total Submissions: 439.1K
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
# WeRide VOE
# TC: O(n*2^n)  SC: O(n*2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, path):
            ans.append(path)
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                dfs(j+1, path+[nums[j]])
        ans = []
        nums.sort()
        dfs(0, [])
        return ans
    
# @lc code=end

