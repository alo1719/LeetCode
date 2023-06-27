#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (76.23%)
# Likes:    1710
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.4M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. recursive
        def dfs(root):
            if not root: return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        ans = []
        dfs(root)
        return ans
        # 2. iterative
        ans, cur, stk = [], root, []
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            # now current is None, meaning cannot go left more
            cur = stk.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
        
# @lc code=end

