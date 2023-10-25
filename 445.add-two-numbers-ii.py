#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (59.69%)
# Likes:    4525
# Dislikes: 247
# Total Accepted:    372.5K
# Total Submissions: 623.9K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# 
# 
# Example 2:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
# 
# Follow up: Could you solve it without reversing the input lists?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n)  SC: O(n)
# can use stack if not allowed to reverse
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        def add(l1, l2):
            dummy = index = ListNode()
            carry_out = 0
            while l1 or l2 or carry_out:
                if l1: carry_out += l1.val
                if l2: carry_out += l2.val
                index.next = ListNode(carry_out%10)
                carry_out //= 10
                index = index.next
                if l1: l1 = l1.next
                if l2: l2 = l2.next
            return dummy.next
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        return reverse(add(l1, l2))
# @lc code=end

