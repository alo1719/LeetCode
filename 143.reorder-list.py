#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.cn/problems/reorder-list/description/
#
# algorithms
# Medium (64.95%)
# Likes:    1330
# Dislikes: 0
# Total Accepted:    276.6K
# Total Submissions: 421.3K
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TC: O(n)  SC: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        # reverse 
        pre, cur = None, mid
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        tail = pre
        # merge
        while tail.next:
            nxt = head.next
            nxt2 = tail.next
            head.next = tail
            tail.next = nxt
            head = nxt
            tail = nxt2
# @lc code=end

