#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#
# https://leetcode.cn/problems/longest-arithmetic-subsequence/description/
#
# algorithms
# Medium (49.31%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 81.8K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array nums of integers, return the length of the longest arithmetic
# subsequence in nums.
# 
# Note that:
# 
# 
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
# (for 0 <= i < seq.length - 1).
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length
# = 3.
# 
# 
# Example 2:
# 
# 
# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].
# 
# 
# Example 3:
# 
# 
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500
# 
# 
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # can be optimized to O(n^2), but hard to think about
        @cache
        def f(i, prev):
            nonlocal n
            ans = 1
            if prev == None:
                for j in range(i+1, n):
                    ans = max(ans, 1+f(j, i))
            else:
                target = nums[i]+nums[i]-nums[prev]
                if target in d and d[target][-1] > i:
                    j = d[target][bisect_right(d[target], i)]
                    ans = max(ans, 1+f(j, i))
            return ans

        n = len(nums)
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        ans = 1
        for i in range(n):
            ans = max(ans, f(i, None))
        return ans
# @lc code=end

