#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Medium (68.73%)
# Likes:    5676
# Dislikes: 1820
# Total Accepted:    595.4K
# Total Submissions: 865.2K
# Testcase Example:  '[0,1,0]'
#
# An array arr a mountain if the following properties hold:
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
# Given a mountain array arr, return the index i such that arr[0] < arr[1] <
# ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# 
# You must solve it in O(log(arr.length)) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: arr = [0,1,0]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: arr = [0,2,1,0]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: arr = [0,10,5,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
# 
# 
#

# @lc code=start
# TC: O(logn)  SC: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1
        while left < right:
            mid1 = (left+right)//2
            mid2 = (left+right)//2+1
            if arr[mid1] > arr[mid2]:
                right = mid1
            else:
                left = mid2
        return left
# @lc code=end

