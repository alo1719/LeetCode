#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (71.35%)
# Likes:    1036
# Dislikes: 0
# Total Accepted:    827.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,2,3]
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
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n)  SC: O(h)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. recursive
        def dfs(root):
            if not root: return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        ans = []
        dfs(root)
        return ans
        # 2. iterative
        ans, cur, stk = [], root, []
        while cur or stk:
            while cur:
                # only traverse/handle in one place
                ans.append(cur.val)
                stk.append(cur)
                cur = cur.left
            # current is now None, meaning cannot go left more
            cur = stk.pop()
            cur = cur.right
        return ans
# @lc code=end

