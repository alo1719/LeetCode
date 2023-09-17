#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.cn/problems/permutations/description/
#
# algorithms
# Medium (78.89%)
# Likes:    2624
# Dislikes: 0
# Total Accepted:    898.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
# TC: O(n*n!)  SC: O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            for j in range(n):
                if not v[j]:
                    v[j] = True
                    path.append(nums[j])
                    dfs(i+1)
                    v[j] = False
                    path.pop()
        ans = []
        path = []
        n = len(nums)
        v = [False]*n
        dfs(0)
        return ans
# @lc code=end

