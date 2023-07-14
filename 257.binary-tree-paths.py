#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.cn/problems/binary-tree-paths/description/
#
# algorithms
# Easy (70.69%)
# Likes:    892
# Dislikes: 0
# Total Accepted:    284.4K
# Total Submissions: 402.3K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
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
# preorder traversal
# TC: O(n^2)  SC: O(n^2) considering need to copy and store all paths
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node.left and not node.right: ans.append(path+str(node.val))
            if node.left: dfs(node.left, path+str(node.val)+'->')
            if node.right: dfs(node.right, path+str(node.val)+'->')
        ans = []
        dfs(root, '')
        return ans
# @lc code=end

