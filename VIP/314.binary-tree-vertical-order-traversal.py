#
# @lc app=leetcode.cn id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#
# https://leetcode.cn/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (55.71%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 16.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left to
# right.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# 
# 
# Example 3:
# 
# 
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC: O(n)  SC: O(n)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, pos = q.popleft()
            ans[pos].append(node.val)
            if node.left:
                q.append((node.left, pos-1))
            if node.right:
                q.append((node.right, pos+1))
        return [ans[pos] for pos in sorted(ans.keys())]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().verticalOrder(root))
# @lc code=end
