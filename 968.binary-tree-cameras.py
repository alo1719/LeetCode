#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (46.49%)
# Likes:    5120
# Dislikes: 67
# Total Accepted:    128.5K
# Total Submissions: 276.5K
# Testcase Example:  '[0,0,null,0,0]'
#
# You are given the root of a binary tree. We install cameras on the tree nodes
# where each camera at a node can monitor its parent, itself, and its immediate
# children.
# 
# Return the minimum number of cameras needed to monitor all nodes of the
# tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# 
# 
# Example 2:
# 
# 
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# Node.val == 0
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # blue: install camera
        # yellow: no camera but father installs camera
        # red: no camera but at least one child installs camera
        # blue = min(left blue, left yellow, left red)+min(right blue, right yellow, right red)+1
        # yellow = min(left blue, left red)+min(right blue, right red)
        # red = min(left blue and right red, left red and right blue, left blue and right blue)
        # ans = min(root blue, root red)
        def dfs(node):
            if not node:
                return inf, 0, 0
            l_choose, l_by_father, l_by_child = dfs(node.left)
            r_choose, r_by_father, r_by_child = dfs(node.right)
            choose = min(l_choose, l_by_father, l_by_child)+min(r_choose, r_by_father, r_by_child)+1
            by_fa = min(l_choose, l_by_child)+min(r_choose, r_by_child)
            by_child = min(l_choose+r_by_child, l_by_child+r_choose, l_choose+r_choose)
            return choose, by_fa, by_child
        choose, _, by_child = dfs(root)
        return min(choose, by_child)
# @lc code=end

