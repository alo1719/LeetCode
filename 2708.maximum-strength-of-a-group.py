#
# @lc app=leetcode id=2708 lang=python3
#
# [2708] Maximum Strength of a Group
#
# https://leetcode.com/problems/maximum-strength-of-a-group/description/
#
# algorithms
# Medium (22.60%)
# Likes:    200
# Dislikes: 25
# Total Accepted:    15.8K
# Total Submissions: 69.3K
# Testcase Example:  '[3,-1,-5,2,5,-9]'
#
# You are given a 0-indexed integer array nums representing the score of
# students in an exam. The teacher would like to form one non-empty group of
# students with maximal strength, where the strength of a group of students of
# indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] *
# ... * nums[ik​].
# 
# Return the maximum strength of a group the teacher can create.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,-1,-5,2,5,-9]
# Output: 1350
# Explanation: One way to form a group of maximal strength is to group the
# students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) =
# 1350, which we can show is optimal.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-4,-5,-4]
# Output: 20
# Explanation: Group the students at indices [0, 1] . Then, we’ll have a
# resulting strength of 20. We cannot achieve greater strength.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 13
# -9 <= nums[i] <= 9
# 
# 
#

# @lc code=start
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        max_neg = maxx = float('-inf')
        selected_num = 0
        for i in range(n):
            if nums[i] != 0:
                ans *= nums[i]
                selected_num += 1
            if nums[i] < 0:
                max_neg = max(max_neg, nums[i])
            maxx = max(maxx, nums[i])
        if selected_num <= 1:
            return maxx
        return ans//max_neg if ans < 0 else ans
# @lc code=end

