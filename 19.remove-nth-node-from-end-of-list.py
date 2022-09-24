#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (39.25%)
# Likes:    12538
# Dislikes: 539
# Total Accepted:    1.7M
# Total Submissions: 4.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a: List[ListNode] = []
        while head:
            a.append(head)
            head = head.next
        if len(a) == 1:
            return None
        if len(a) == n:
            return a[1]
        a[-(n + 1)].next = a[-n].next
        return a[0]

# @lc code=end
