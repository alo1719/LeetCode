#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (76.32%)
# Likes:    1015
# Dislikes: 0
# Total Accepted:    601.1K
# Total Submissions: 787.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# The number of the nodes in the tree is in the range [0, 100].
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

# TC: O(n)  SC: O(h)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. recursive
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        ans = []
        dfs(root)
        return ans
        # 2. iterative (need prev, complicated)
        ans, cur, stk, pre = [], root, [], None
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left  # left
            # now current is None, meaning cannot left anymore
            cur = stk[-1]
            if cur.right and cur.right != pre:
                cur = cur.right  # right
            else:
                stk.pop()
                ans.append(cur.val) # root
                pre = cur
                cur = None  # important, do not traverse it again
        return ans
# @lc code=end

