#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (82.63%)
# Likes:    4583
# Dislikes: 307
# Total Accepted:    151.7K
# Total Submissions: 183.6K
# Testcase Example:  '7'
#
# Given an integer n, return a list of all possible full binary trees with n
# nodes. Each node of each tree in the answer must have Node.val == 0.
# 
# Each element of the answer is the root node of one possible tree. You may
# return the final list of trees in any order.
# 
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# 
# Example 1:
# 
# 
# Input: n = 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: [[0,0,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
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
# TC: O(2^n)  SC: O(2^n)  hard to analyze
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0: return []
        if n == 1: return [TreeNode()]
        left = 1
        right = n-2
        ans = []
        while right > 0:
            left_tree = self.allPossibleFBT(left)
            right_tree = self.allPossibleFBT(right)
            for l, r in product(left_tree, right_tree):
                    ans.append(TreeNode(0, l, r))
            left += 2
            right -= 2
        return ans
# @lc code=end

