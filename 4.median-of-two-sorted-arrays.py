#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (41.63%)
# Likes:    6201
# Dislikes: 0
# Total Accepted:    873.2K
# Total Submissions: 2.1M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth_element(k):
            i1, i2 = 0, 0

            while True:
                if i1 == m:
                    return nums2[i2 + k - 1]
                if i2 == n:
                    return nums1[i1 + k - 1]
                if k == 1:
                    return min(nums2[i2], nums1[i1])
                
                new_i1 = min(i1 + k // 2 - 1, m - 1)
                new_i2 = min(i2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[new_i1], nums2[new_i2]
                if pivot1 > pivot2:
                    k -= new_i2 - i2 + 1
                    i2 = new_i2 + 1
                else:
                    k -= new_i1 - i1 + 1
                    i1 = new_i1 + 1


        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 == 1:
            return get_kth_element(total // 2 + 1)
        else:
            return (get_kth_element(total // 2) + get_kth_element(total // 2 + 1)) / 2
# @lc code=end

