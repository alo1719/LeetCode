#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (72.39%)
# Likes:    941
# Dislikes: 0
# Total Accepted:    322.7K
# Total Submissions: 445.8K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000
# 
# 
# 
# Follow-up:
# 
# 
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Snowflake VOE, good question!
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 1. BFS, TC: O(n)  SC: O(n)
        # if not root: return root
        # dq = deque([root])
        # while dq:
        #     cnt = len(dq)
        #     for _ in range(cnt):
        #         node = dq.popleft()
        #         if node.left:
        #             dq.append(node.left)
        #             dq.append(node.right)
        #     for i in range(len(dq)-1):
        #         dq[i].next = dq[i+1]
        # return root
        # 2. O(1) space, note that the previous level is already connected
        if not root: return root
        leftmost = root
        while leftmost.left:
            cur = leftmost
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            leftmost = leftmost.left
        return root
    
    def connect_not_perfect(self, root):
        if not root: return root
        leftmost = root
        while leftmost:
            cur = leftmost
            leftmost = None
            while cur:
                if cur.left and cur.right: cur.left.next = cur.right
                right_has_child = cur.next
                while right_has_child and not right_has_child.left and not right_has_child.right:
                    right_has_child = right_has_child.next
                if right_has_child:
                    if cur.right:
                        cur.right.next = right_has_child.left if right_has_child.left else right_has_child.right
                    elif cur.left:
                        cur.left.next = right_has_child.left if right_has_child.left else right_has_child.right
                if not leftmost:
                    if cur.left: leftmost = cur.left
                    elif cur.right: leftmost = cur.right
                cur = cur.next
        return root
# @lc code=end

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n7 = Node(7)
n9 = Node(9)
n15 = Node(15)
n18 = Node(18)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n7
n4.right = n9
n7.right = n15
n18.left = n18
Solution().connect_not_perfect(n1)
print(n2.next==n3)
print(n4.next==n5)
print(n5.next==n7)
print(n9.next==n15)
print(not n18.next)
