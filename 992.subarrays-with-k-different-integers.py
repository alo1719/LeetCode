#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.cn/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (47.25%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    30.3K
# Total Submissions: 64.1K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an integer array nums and an integer k, return the number of good
# subarrays of nums.
# 
# A good array is an array where the number of different integers in that array
# is exactly k.
# 
# 
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# 
# 
# A subarray is a contiguous part of an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i], k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n, right_start, right_end, dict, ans = len(nums), -1, -1, defaultdict(int), 0
        for left in range(n):
            if left > 0:
                dict[nums[left-1]] -= 1
                if dict[nums[left-1]] == 0: del dict[nums[left-1]]
            while right_start+1 < n and len(dict) < k:
                right_start += 1
                dict[nums[right_start]] += 1
            while right_end+1 < n and len(dict) == k and nums[right_end+1] in dict:
                right_end += 1
            if right_end >= right_start and len(dict) == k:
                ans += right_end-right_start+1
        return ans
# @lc code=end

