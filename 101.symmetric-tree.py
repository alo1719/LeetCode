#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (52.70%)
# Likes:    11092
# Dislikes: 253
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(n)  SC: O(n)
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        @cache
        def dfs(i, j):
            if not i and not j: return True
            if not i or not j: return False
            return i.val == j.val and dfs(i.left, j.right) and dfs(i.right, j.left)

        return dfs(root, root)
# @lc code=end
