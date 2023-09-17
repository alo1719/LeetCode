#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.cn/problems/subsets/description/
#
# algorithms
# Medium (81.12%)
# Likes:    2101
# Dislikes: 0
# Total Accepted:    653.8K
# Total Submissions: 805.8K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
# TC: O(n*2^n)  SC: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            dfs(i+1)  # not choose
            path.append(nums[i])
            dfs(i+1)  # choose
            path.pop()
        ans = []
        path = []
        n = len(nums)
        dfs(0)
        return ans
# @lc code=end

