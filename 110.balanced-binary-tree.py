#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (57.56%)
# Likes:    1369
# Dislikes: 0
# Total Accepted:    522.2K
# Total Submissions: 907.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            if left == -1: return -1
            right = dfs(node.right)
            if right == -1 or abs(left-right) > 1: return -1
            return max(left, right)+1
        return dfs(root) != -1
# @lc code=end

