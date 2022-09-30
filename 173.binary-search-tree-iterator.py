#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.cn/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (81.36%)
# Likes:    647
# Dislikes: 0
# Total Accepted:    103.7K
# Total Submissions: 127.5K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
# '[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]'
#
# Implement the BSTIterator class that represents an iterator over the in-order
# traversal of a binary search tree (BST):
#
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
# The root of the BST is given as part of the constructor. The pointer should
# be initialized to a non-existent number smaller than any element in the
# BST.
# boolean hasNext() Returns true if there exists a number in the traversal to
# the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the
# pointer.
#
#
# Notice that by initializing the pointer to a non-existent smallest number,
# the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be
# at least a next number in the in-order traversal when next() is called.
#
#
# Example 1:
#
#
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next",
# "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
#
# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.
#
#
#
# Follow up:
#
#
# Could you implement next() and hasNext() to run in average O(1) time and use
# O(h) memory, where h is the height of the tree?
#
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val

    def hasNext(self) -> bool:
        if self.cur or self.stack:
            return True
        return False


root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
i = BSTIterator(root)
print(i.next())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())

# @lc code=end
