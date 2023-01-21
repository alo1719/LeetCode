#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.cn/problems/add-two-numbers/description/
#
# algorithms
# Medium (42.31%)
# Likes:    9105
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 3.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = index = ListNode(None)
        carry_out = 0
        while l1 or l2 or carry_out:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1.next else l1
            l2 = l2.next if l2.next else l2
            now_value = (v1 + v2 + carry_out) % 10
            carry_out = (v1 + v2 + carry_out) // 10
            tmp = ListNode(now_value, None)
            index.next = tmp
            index = index.next
        return head
# @lc code=end

