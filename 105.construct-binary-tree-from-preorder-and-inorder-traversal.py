#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (62.51%)
# Likes:    13940
# Dislikes: 423
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TC: O(n)  SC: O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(p_left, p_right, i_left, i_right):
            if p_left > p_right: return None
            # p_left, p_right, i_left, i_right, p_root, i_root are all indices
            p_root = p_left
            i_root = d[preorder[p_root]]
            root = TreeNode(preorder[p_root])
            left_size = i_root-i_left
            root.left = dfs(p_left+1, p_left+left_size, i_left, i_root-1)
            root.right = dfs(p_left+left_size+1, p_right, i_root+1, i_right)
            return root
        n = len(preorder)
        d = {v:i for i, v in enumerate(inorder)}
        return dfs(0, n-1, 0, n-1)
    
    # TC: O(n^2)  SC: O(n^2)
    def buildTreeLevel(self, level: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(i_left, i_right, level):
            if i_left > i_right: return None
            i_root = d[level[0]]
            root = TreeNode(level[0])
            left_level = [v for v in level if i_left <= d[v] < i_root]
            right_level = [v for v in level if i_root < d[v] <= i_right]
            root.left = dfs(i_left, i_root-1, left_level)
            root.right = dfs(i_root+1, i_right, right_level)
            return root
        n = len(level)
        d = {v:i for i, v in enumerate(inorder)}
        return dfs(0, n-1, level)
    
a = Solution().buildTreeLevel([20,8,22,4,12,10,14], [4,8,10,12,14,20,22])
b = Solution().buildTreeLevel([3,9,20,4,15,7], [4,9,3,15,20,7])
# @lc code=end

