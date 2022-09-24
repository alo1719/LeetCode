#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (61.61%)
# Likes:    15002
# Dislikes: 1321
# Total Accepted:    2.6M
# Total Submissions: 4.3M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
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


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = Solution().mergeTwoLists(a, b)
while c:
    print(c.val)
    c = c.next

# @lc code=end
