#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (68.65%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    465.9K
# Total Submissions: 678.7K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
# 
# 
# 
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 2 pointers
        n, i = len(nums), 0
        while nums[i] < 0 and i < n - 1:
            i += 1
        left, right = i, i - 1
        ans = []
        while left > 0 or right < n - 1:
            if left <= 0:
                ans.append(nums[right+1]**2)
                right += 1
            elif right >= n - 1:
                ans.append(nums[left - 1] ** 2)
                left -= 1
            elif abs(nums[left-1]) > nums[right+1]:
                ans.append(nums[right+1]**2)
                right += 1
            else:
                ans.append(nums[left-1]**2)
                left -= 1
        return ans
# @lc code=end

