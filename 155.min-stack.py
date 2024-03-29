#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Medium (51.54%)
# Likes:    9670
# Dislikes: 678
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
'[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# Implement the MinStack class:
#
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
#
#
# You must implement a solution with O(1) time complexity for each function.
#
#
# Example 1:
#
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
#
# Constraints:
#
#
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
#
#
#

# @lc code=start

# TC: O(1)  SC: O(n)
class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.min_stk.append(min(self.min_stk[-1] if self.min_stk else inf, val))

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
