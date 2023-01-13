#
# @lc app=leetcode.cn id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
# https://leetcode.cn/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (72.12%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    18.6K
# Total Submissions: 25.9K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
# 
# Implement the MovingAverage class:
# 
# 
# MovingAverage(int size) Initializes the object with the size of the window
# size.
# double next(int val) Returns the moving average of the last size values of
# the stream.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]
# 
# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= size <= 1000
# -10^5 <= val <= 10^5
# At most 10^4 calls will be made to next.
# 
# 
#

# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = []

    def next(self, val: int) -> float:
        self.q.append(val)
        if len(self.q) > self.size:
            self.q.pop(0)
        # print(sum(self.q) / len(self.q))
        return sum(self.q) / len(self.q)


movingAverage = MovingAverage(3);
movingAverage.next(1);
movingAverage.next(10);
movingAverage.next(3);
movingAverage.next(5);

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end
