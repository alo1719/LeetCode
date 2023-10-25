#
# @lc app=leetcode.cn id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#
# https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
#
# algorithms
# Medium (44.61%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 18K
# Testcase Example:  '[5,1,2,3,null,6,4]\n3\n6'
#
# You are given the root of a binary tree with n nodes. Each node is uniquely
# assigned a value from 1 to n. You are also given an integer startValue
# representing the value of the start node s, and a different integer destValue
# representing the value of the destination node t.
# 
# Find the shortest path starting from node s and ending at node t. Generate
# step-by-step directions of such path as a string consisting of only the
# uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific
# direction:
# 
# 
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# 
# 
# Return the step-by-step directions of the shortest path from node s to node
# t.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is n.
# 2 <= n <= 10^5
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue
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
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # TC: O(n), SC: O(n)
        def dfs(node, val, path):
            if not node: return False
            if node.val == val: return True
            if node.left:
                path.append('L')
                if dfs(node.left, val, path): return True
                path.pop()
            if node.right:
                path.append('R')
                if dfs(node.right, val, path): return True
                path.pop()
        p2s = []
        p2d = []
        dfs(root, startValue, p2s)
        dfs(root, destValue, p2d)
        idx = 0
        while idx < len(p2s) and idx < len(p2d) and p2s[idx] == p2d[idx]:
            idx += 1
        return 'U'*(len(p2s)-idx)+''.join(p2d[idx:])
# @lc code=end

