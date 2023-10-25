#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.cn/problems/path-sum-ii/description/
#
# algorithms
# Medium (63.21%)
# Likes:    1038
# Dislikes: 0
# Total Accepted:    366.6K
# Total Submissions: 580K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where the sum of the node values in the path equals
# targetSum. Each path should be returned as a list of the node values, not
# node references.
# 
# A root-to-leaf path is a path starting from the root and ending at any leaf
# node. A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3], targetSum = 5
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], targetSum = 0
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node):
            nonlocal S
            if not node: return
            path.append(node.val)
            S += node.val
            dfs(node.left)
            if node.left:
                S -= node.left.val
                path.pop()
            if not node.left and not node.right:
            	if S == targetSum:
                    ans.append(path[:])
            dfs(node.right)
            if node.right:
                S -= node.right.val
                path.pop()
        path = []
        ans = []
        S = 0
        dfs(root)
        return ans
# @lc code=end

