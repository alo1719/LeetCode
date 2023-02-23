#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
# https://leetcode.cn/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (54.58%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    46.4K
# Total Submissions: 84.9K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a binary tree, determine if it is a complete binary tree.
# 
# In a complete binary tree, every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level
# h.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left
# as possible.
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
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
from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append(root)
        none_exisit = False
        while dq:
            node = dq.popleft()
            if not node:
                none_exisit = True
            else:
                if none_exisit: return False
                dq.append(node.left)
                dq.append(node.right)
        return True
# @lc code=end

