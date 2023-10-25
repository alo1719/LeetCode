#
# @lc app=leetcode.cn id=996 lang=python3
#
# [996] Number of Squareful Arrays
#
# https://leetcode.cn/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (49.95%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 12.7K
# Testcase Example:  '[1,17,8]'
#
# An array is squareful if the sum of every pair of adjacent elements is a
# perfect square.
# 
# Given an integer array nums, return the number of permutations of nums that
# are squareful.
# 
# Two permutations perm1 and perm2 are different if there is some index i such
# that perm1[i] != perm2[i].
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,17,8]
# Output: 2
# Explanation: [1,8,17] and [17,8,1] are the valid permutations.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 12
# 0 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        ans=0
        def dfs(nums, now):
            nonlocal ans
            if not nums:
                ans += 1
                return
            for i in range(len(nums)):
                if nums[i] in nums[:i]:
                    continue
                if not now or math.sqrt(now[-1]+nums[i])%1 == 0:
                    dfs(nums[:i]+nums[i+1:],now+[nums[i]])
        dfs(nums,[])
        return ans
# @lc code=end
