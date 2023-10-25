#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.38%)
# Likes:    5133
# Dislikes: 210
# Total Accepted:    153.5K
# Total Submissions: 352.9K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
# 
# Notice that the sequence has to be strictly increasing.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there
# are 5 increasing subsequences of length 1, so output 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
# 
# 
#

# @lc code=start
# TC: O(n^2)  SC: O(n)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # f[i] = max_sum(f[j][0]), max(f[j][1])+1  j < i, nums[j] < nums[i]
        #          cnt            lenn 
        @cache
        def f(i):
            cnt, lenn = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    jcnt, jlen = f(j)
                    if jlen > lenn:
                        lenn = jlen
                        cnt = jcnt
                    elif jlen == lenn:
                        cnt += jcnt
            return cnt, lenn+1
        n = len(nums)
        max_len = max(f(i)[1] for i in range(n))
        return sum(f(i)[0] for i in range(n) if f(i)[1] == max_len)
# @lc code=end

