#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (61.05%)
# Likes:    8624
# Dislikes: 501
# Total Accepted:    834.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
#
# Example 2:
#
#
# Input: root = [1,null,3]
# Output: [1,3]
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
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(n)  SC: O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        dq = deque([root])
        ans = []
        while dq:
            lenn = len(dq)
            ans.append(dq[-1].val)
            for _ in range(lenn):
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
        return ans


Solution().rightSideView(TreeNode(1, TreeNode(
    2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))))

# @lc code=end
