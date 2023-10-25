#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.cn/problems/valid-mountain-array/description/
#
# algorithms
# Easy (39.53%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    79.5K
# Total Submissions: 201.2K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
# Snowflake VOE
class Solution:
    def validMountainArray(self, arr) -> bool:
        n = len(arr)
        if n < 3: return False # so n >= 3
        index = 0
        while index+1 <= n-1 and arr[index+1] > arr[index]:
            index += 1
        if index == 0 or index == n-1: return False
        while index+1 <= n-1 and arr[index+1] < arr[index]:
            index += 1
        return index == n-1
# @lc code=end

