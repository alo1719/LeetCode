#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (45.39%)
# Likes:    1691
# Dislikes: 0
# Total Accepted:    271.4K
# Total Submissions: 597.8K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        sum = 0
        ans = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans += prefix.get(sum - k, 0)
            prefix[sum] = prefix.get(sum, 0) + 1
            ans += 1 if sum == k else 0
        print(ans)
        return ans


Solution().subarraySum([1, 1, 1], 2)
Solution().subarraySum([1, 2, 3], 3)
# @lc code=end

