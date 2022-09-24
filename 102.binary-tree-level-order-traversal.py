#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (62.99%)
# Likes:    10901
# Dislikes: 207
# Total Accepted:    1.5M
# Total Submissions: 2.4M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
#
#

# @lc code=start
from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a queue to store the nodes of each level
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            result.append([node.val for node in queue])
            queue = [
                child for node in queue for child in (node.left, node.right)
                if child
            ]
        return result


a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().levelOrder(a))
# @lc code=end
