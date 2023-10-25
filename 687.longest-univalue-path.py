#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.cn/problems/longest-univalue-path/description/
#
# algorithms
# Medium (47.57%)
# Likes:    750
# Dislikes: 0
# Total Accepted:    79.4K
# Total Submissions: 166.8K
# Testcase Example:  '[5,4,5,1,1,null,5]'
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.
# 
# The length of the path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 5).
# 
# 
# Example 2:
# 
# 
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 4).
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
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
# Snowflake VOE
# TC: O(n), SC: O(n)
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # postorder traversal
        def dfs(root):
            nonlocal ans
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left_ans = left+1 if root.left and root.left.val == root.val else 0
            right_ans = right+1 if root.right and root.right.val == root.val else 0
            ans = max(ans, left_ans+right_ans)
            return max(left_ans, right_ans)

        ans = 0
        dfs(root)
        return ans
# @lc code=end

