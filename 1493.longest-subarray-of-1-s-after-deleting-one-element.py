#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/description/
#
# algorithms
# Medium (60.35%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 42.5K
# Testcase Example:  '[1,1,0,1]'
#
# Given a binary array nums, you should delete one element from it.
# 
# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array. Return 0 if there is no such subarray.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3
# numbers with value of 1's.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1]
# longest subarray with value of 1's is [1,1,1,1,1].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        @cache
        def f(i, removed):
            if i == 0:
                if removed: return 0
                else: return nums[i]
            if not removed:
                if not nums[i]: return 0
                else: return 1+f(i-1, False)
            else:
                if nums[i]: return max(f(i-1, False), f(i-1, True)+1)
                else: return max(f(i-1, False), 0)
        n = len(nums)
        return max([f(i, True) for i in range(n)])
# @lc code=end

