#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (72.08%)
# Likes:    14708
# Dislikes: 249
# Total Accepted:    2.5M
# Total Submissions: 3.5M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# WeRide VOE
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Iterative
        #  1 -> 2 -> 3 -> 4 -> 5
        #  p1  p2  p3
        #                p1   p2
        # TC: O(n)  SC: O(1)
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
        # 2. Recursive
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3 -> 4 <- 5
        #          head
        # TC: O(n)  SC: O(n)
        if not head or not head.next: return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None  # make sure first node's next is None
        return new_head

# @lc code=end
