#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#
# https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
#
# algorithms
# Medium (72.29%)
# Likes:    4665
# Dislikes: 153
# Total Accepted:    104K
# Total Submissions: 143.8K
# Testcase Example:  '[3,0,0]'
#
# You are given the root of a binary tree with n nodes where each node in the
# tree has node.val coins. There are n coins in total throughout the whole
# tree.
# 
# In one move, we may choose two adjacent nodes and move one coin from one node
# to another. A move may be from parent to child, or from child to parent.
# 
# Return the minimum number of moves required to make every node have exactly
# one coin.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child,
# and one coin to its right child.
# 
# 
# Example 2:
# 
# 
# Input: root = [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root
# [taking two moves]. Then, we move one coin from the root of the tree to the
# right child.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is n.
# 1 <= n <= 100
# 0 <= Node.val <= n
# The sum of all Node.val is n.
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            nonlocal ans
            if not node: return
            if node.left: dfs(node.left, node)
            if node.right: dfs(node.right, node)
            if node.val > 1:
                parent.val += node.val-1
                ans += node.val-1
            if node.val < 1:
                parent.val -= 1-node.val
                ans += 1-node.val
        ans = 0
        dfs(root, None)
        return ans
# @lc code=end

