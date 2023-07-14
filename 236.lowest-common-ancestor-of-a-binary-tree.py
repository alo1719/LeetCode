#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (57.71%)
# Likes:    12440
# Dislikes: 307
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
#
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# TC: O(n)  SC: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # classic classify question with postorder
        # cur is None -> return None
        # cur is p -> return p
        # cur is q -> return q
        # found in both left and right subtree -> return root
        # found in left subtree -> return left (because it's postorder, return to root)
        # found in right subtree -> return right
        # both left and right subtree not found -> return None
        if not root: return None
        if root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)  # if found in left subtree, return left
        right = self.lowestCommonAncestor(root.right, p, q)  # if found in right subtree, return right
        if left and right: return root
        elif left: return left
        else: return right

TreeNode1 = TreeNode(3)
TreeNode2 = TreeNode(5)
TreeNode3 = TreeNode(1)
TreeNode4 = TreeNode(6)
TreeNode5 = TreeNode(2)
TreeNode6 = TreeNode(0)
TreeNode7 = TreeNode(8)
TreeNode8 = TreeNode(7)
TreeNode9 = TreeNode(4)
TreeNode1.left = TreeNode2
TreeNode1.right = TreeNode3
TreeNode2.left = TreeNode4
TreeNode2.right = TreeNode5
TreeNode3.left = TreeNode6
TreeNode3.right = TreeNode7
TreeNode5.left = TreeNode8
TreeNode5.right = TreeNode9
Solution().lowestCommonAncestor(TreeNode1, TreeNode4, TreeNode8)
# @lc code=end
