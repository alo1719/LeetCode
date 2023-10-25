#
# @lc app=leetcode.cn id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#
# https://leetcode.cn/problems/linked-list-in-binary-tree/description/
#
# algorithms
# Medium (43.53%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 52.7K
# Testcase Example:  '[4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'
#
# Given a binary tree root and a linked list with head as the first node. 
# 
# Return True if all the elements in the linked list starting from the head
# correspond to some downward path connected in the binary tree otherwise
# return False.
# 
# In this context downward path means a path that starts at some node and goes
# downwards.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: head = [4,2,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.  
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: head = [1,4,2,6], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: head = [1,4,2,6,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the
# elements of the linked list from head.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [1, 2500].
# The number of nodes in the list will be in the range [1, 100].
# 1 <= Node.val <= 100 for each node in the linked list and binary tree.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Snowflake VOE, Good question!
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def try_match(root, current):
            if not root: return False
            if root.val != current.val: return False
            if current.next:
                return try_match(root.left, current.next) or try_match(root.right, current.next)
            return True
        
        def dfs(root):
            nonlocal is_sub_path
            if is_sub_path: return
            if not root: return
            if root.val == head.val:
                is_sub_path = try_match(root, head)
            dfs(root.left)
            dfs(root.right)

        is_sub_path = False
        dfs(root)
        return is_sub_path
# @lc code=end

