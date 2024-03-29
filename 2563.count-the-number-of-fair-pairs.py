#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#
# https://leetcode.cn/problems/count-the-number-of-fair-pairs/description/
#
# algorithms
# Medium (32.24%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 17.7K
# Testcase Example:  '[0,1,7,4,4,5]\n3\n6'
#
# Given a 0-indexed integer array nums of size n and two integers lower and
# upper, return the number of fair pairs.
# 
# A pair (i, j) is fair if:
# 
# 
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and
# (1,5).
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums.length == n
# -10^9 <= nums[i] <= 10^9
# -10^9 <= lower <= upper <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sliding window (enhanced version)
        nums, n = sorted(nums), len(nums)
        left, right_start, right_end, ans = 0, n, n, 0  # [right_start, right_end)
        for left in range(n-1):
            while right_start-1 >= 0 and nums[left]+nums[right_start-1] >= lower:
                right_start -= 1
            while right_end-1 >= 0 and nums[left]+nums[right_end-1] > upper:
                right_end -= 1
            if right_end > left+1:
                ans += right_end-max(right_start, left+1)
        return ans
# @lc code=end

