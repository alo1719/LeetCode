#
# @lc app=leetcode.cn id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
#
# algorithms
# Medium (79.72%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 5.6K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given two nodes of a binary tree p and q, return their lowest common ancestor
# (LCA).
# 
# Each node will have a reference to its parent node. The definition for Node
# is below:
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public Node left;
# ⁠   public Node right;
# ⁠   public Node parent;
# }
# 
# 
# According to the definition of LCA on Wikipedia: "The lowest common ancestor
# of two nodes p and q in a tree T is the lowest node that has both p and q as
# descendants (where we allow a node to be a descendant of itself)."
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
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant
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
# p and q exist in the tree.
# 
# 
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# TC: O(n)  SC: O(1), n is the depth of the tree
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        left = p
        right = q
        # two pointer problem
        while left != right:
            left = left.parent if left.parent else q # if hit root, go to the other node
            right = right.parent if right.parent else p
        return left

p = Node(5)
q = Node(1)
p.left = Node(6)
p.right = Node(2)
p.left.parent = p
p.right.parent = p
p.right.left = Node(7)
p.right.right = Node(4)
p.right.left.parent = p.right
p.right.right.parent = p.right
q.left = Node(0)
q.right = Node(8)
q.left.parent = q
q.right.parent = q
parent = Node(3)
p.parent = parent
q.parent = parent
Solution().lowestCommonAncestor(p.left, p.right.right)
# @lc code=end
