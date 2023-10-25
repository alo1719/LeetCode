#
# @lc app=leetcode.cn id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#
# https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/description/
#
# algorithms
# Hard (44.76%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 15.5K
# Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
#
# You are given an integer array nums and two integers minK and maxK.
# 
# A fixed-bound subarray of nums is a subarray that satisfies the following
# conditions:
# 
# 
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# 
# 
# Return the number of fixed-bound subarrays.
# 
# A subarray is a contiguous part of an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
# possible subarrays.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# 1 <= nums[i], minK, maxK <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        ans = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == min_k: min_i = i
            if x == max_k: max_i = i
            if not min_k <= x <= max_k: i0 = i  # 子数组不能包含 nums[i0]
            j = min_i if min_i < max_i else max_i
            if j > i0: ans += j-i0
        return ans
# @lc code=end

