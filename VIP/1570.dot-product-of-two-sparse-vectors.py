#
# @lc app=leetcode.cn id=1570 lang=python3
#
# [1570] Dot Product of Two Sparse Vectors
#
# https://leetcode.cn/problems/dot-product-of-two-sparse-vectors/description/
#
# algorithms
# Medium (89.15%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 4.4K
# Testcase Example:  '[1,0,0,2,3]\n[0,3,0,4,0]'
#
# Given two sparse vectors, compute their dot product.
# 
# Implement class SparseVector:
# 
# 
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector
# and vec
# 
# 
# A sparse vector is a vector that has mostly zero values, you should store the
# sparse vector efficiently and compute the dot product between two
# SparseVector.
# 
# Follow up: What if only one of the vectors is sparse?
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start
from typing import List

# TC: O(n)  SC: O(k) where k is the number of non-zero elements in the vector
class SparseVector:

    def __init__(self, nums: List[int]):
        self.vec = {}
        for i, v in enumerate(nums):
            if v:
                self.vec[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, v in self.vec.items():
            if i in vec.vec:
                ans += v * vec.vec[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
ans = v1.dotProduct(v2)
print(ans)
# @lc code=end
