#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (58.74%)
# Likes:    1385
# Dislikes: 0
# Total Accepted:    334.7K
# Total Submissions: 569.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
# 
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges
# between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def f(node):
            nonlocal ans
            if not node: return -1
            left = f(node.left)
            right = f(node.right)
            ans = max(ans, left+right+2)  # -1-1+2=0
            return max(left, right)+1
        ans = 0
        f(root)
        return ans
# @lc code=end

