#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (73.45%)
# Likes:    1463
# Dislikes: 0
# Total Accepted:    172.3K
# Total Submissions: 234.6K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
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
# TC: O(n*Gn)  SC: O(n*Gn)  Gn is Catalan number, also number of BSTs
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(b, e):
            if b > e: return [None]
            ans = []
            for i in range(b, e+1):
                left = dfs(b, i-1)
                right = dfs(i+1, e)
                for l in left:
                    for r in right:
                        ans.append(TreeNode(i, l, r))
            return ans
        return dfs(1, n)
# @lc code=end

