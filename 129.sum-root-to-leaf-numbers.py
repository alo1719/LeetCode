#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (69.79%)
# Likes:    583
# Dislikes: 0
# Total Accepted:    186.7K
# Total Submissions: 267.5K
# Testcase Example:  '[1,2,3]'
#
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
#
#
# Return the total sum of all root-to-leaf numbers. Test cases are generated so
# that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
#
# Example 2:
#
#
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
#
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(n)  SC: O(n)
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur):
            if not root.left and not root.right: return 10*cur+root.val
            ans = 0
            if root.left: ans += dfs(root.left, 10*cur+root.val)
            if root.right: ans += dfs(root.right, 10*cur+root.val)
            return ans

        return dfs(root, 0)
# Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3)))
Solution().sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)))
# @lc code=end
