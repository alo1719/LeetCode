#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.cn/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (73.42%)
# Likes:    504
# Dislikes: 0
# Total Accepted:    198K
# Total Submissions: 269.8K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC: O(n)  SC: O(n)
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.right: dq.append(node.right)
            if node.left: dq.append(node.left)
        return node.val
# @lc code=end

