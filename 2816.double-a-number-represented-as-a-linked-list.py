#
# @lc app=leetcode.cn id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#
# https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/description/
#
# algorithms
# Medium (55.05%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 9.3K
# Testcase Example:  '[1,8,9]'
#
# You are given the head of a non-empty linked list representing a non-negative
# integer without leading zeroes.
# 
# Return the head of the linked list after doubling it.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which
# represents the number 189. Hence, the returned linked list represents the
# number 189 * 2 = 378.
# 
# 
# Example 2:
# 
# 
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which
# represents the number 999. Hence, the returned linked list reprersents the
# number 999 * 2 = 1998. 
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^4]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not
# have leading zeros, except the number 0 itself.
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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            head = ListNode(0, head)
        cur = head
        while cur:
            cur.val = cur.val*2%10
            if cur.next and cur.next.val >= 5:
                cur.val += 1
            cur = cur.next
        return head
# @lc code=end

