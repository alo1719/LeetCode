#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (42.72%)
# Likes:    7587
# Dislikes: 1021
# Total Accepted:    301.1K
# Total Submissions: 705K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return the maximum width of the given tree.
# 
# The maximum width of a tree is the maximum width among all levels.
# 
# The width of one level is defined as the length between the end-nodes (the
# leftmost and rightmost non-null nodes), where the null nodes between the
# end-nodes that would be present in a complete binary tree extending down to
# that level are also counted into the length calculation.
# 
# It is guaranteed that the answer will in the range of a 32-bit signed
# integer.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4
# (5,3,null,9).
# 
# 
# Example 2:
# 
# 
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7
# (6,null,null,null,null,null,7).
# 
# 
# Example 3:
# 
# 
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2
# (3,2).
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append((root, 0))
        ans = 0
        while dq:
            lenn = len(dq)
            minn = float("inf")
            maxx = -1
            for _ in range(lenn):
                node, no = dq.popleft()
                minn = min(minn, no)
                maxx = max(maxx, no)
                if node.left:
                    dq.append((node.left, no*2+1))
                if node.right:
                    dq.append((node.right, no*2+2))
            ans = max(ans, maxx-minn+1 if maxx != minn else 1)
        return ans
# @lc code=end

