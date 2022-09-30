#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.40%)
# Likes:    1901
# Dislikes: 0
# Total Accepted:    749.7K
# Total Submissions: 1.2M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
# You must solve it in O(n) time complexity.
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right, k):
            pivot = nums[left]
            l, r = left, right
            while l < r:
                while l < r and nums[r] <= pivot:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] >= pivot:
                    l += 1
                nums[r] = nums[l]
            nums[l] = pivot
            if l == k:
                print(nums[l])
                return nums[l]
            elif l < k:
                return partition(nums, l + 1, right, k)
            else:
                return partition(nums, left, l - 1, k)

        return partition(nums, 0, len(nums) - 1, k-1)


Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)

# @lc code=end
