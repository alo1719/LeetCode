#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#
# https://leetcode.com/problems/my-calendar-iii/description/
#
# algorithms
# Hard (71.54%)
# Likes:    1861
# Dislikes: 255
# Total Accepted:    84.9K
# Total Submissions: 118.7K
# Testcase Example:  '["MyCalendarThree","book","book","book","book","book","book"]\n' +
# '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# A k-booking happens when k events have some non-empty intersection (i.e.,
# there is some time that is common to all k events.)
# 
# You are given some events [startTime, endTime), after each given event,
# return an integer k representing the maximum k-booking between all the
# previous events.
# 
# Implement the MyCalendarThree class:
# 
# 
# MyCalendarThree() Initializes the object.
# int book(int startTime, int endTime) Returns an integer k representing the
# largest integer such that there exists a k-booking in the calendar.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, 1, 1, 2, 3, 3, 3]
# 
# Explanation
# MyCalendarThree myCalendarThree = new MyCalendarThree();
# myCalendarThree.book(10, 20); // return 1
# myCalendarThree.book(50, 60); // return 1
# myCalendarThree.book(10, 40); // return 2
# myCalendarThree.book(5, 15); // return 3
# myCalendarThree.book(5, 10); // return 3
# myCalendarThree.book(25, 55); // return 3
# 
# 
# 
# 
# Constraints:
# 
# 
# 0 <= startTime < endTime <= 10^9
# At most 400 calls will be made to book.
# 
# 
#

# @lc code=start
class Node:
    def __init__(self, L, R):
        self.left = None
        self.right = None
        self.M = (L+R)//2
        self.L = L
        self.R = R
        # need custimize
        self.maxx = 0
        self.lazy_add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node(1, 10**9+1)

    def update(self, L, R, V, node=None):
        if L > R: return
        if not node: node = self.root
        if node.L >= L and node.R <= R:
            # need custimize
            node.maxx += V
            node.lazy_add += V
            return
        self.pushdown(node)
        if L <= node.M: self.update(L, R, V, node.left)
        if R > node.M: self.update(L, R, V, node.right)
        self.pushup(node)

    def query(self, L, R, node=None):
        if L > R: return 0
        if not node: node = self.root
        if node.L >= L and node.R <= R:
            # need custimize
            return node.maxx
        self.pushdown(node)
        # need custimize
        maxx = 0
        if L <= node.M: maxx = max(maxx, self.query(L, R, node.left))
        if R > node.M: maxx = max(maxx, self.query(L, R, node.right))
        return maxx

    def pushup(self, node):
        # need custimize
        node.maxx = max(node.left.maxx, node.right.maxx)

    def pushdown(self, node):
        if not node.left: node.left = Node(node.L, node.M)
        if not node.right: node.right = Node(node.M+1, node.R)
        # need custimize
        if node.lazy_add:
            node.left.maxx += node.lazy_add
            node.right.maxx += node.lazy_add
            node.left.lazy_add += node.lazy_add
            node.right.lazy_add += node.lazy_add
            node.lazy_add = 0

class MyCalendarThree:

    def __init__(self):
        self.segtree = SegmentTree()

    def book(self, startTime: int, endTime: int) -> int:
      self.segtree.update(startTime+1, endTime, 1)
      return self.segtree.query(1, 10**9+1)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

