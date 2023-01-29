#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.cn/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (52.16%)
# Likes:    503
# Dislikes: 0
# Total Accepted:    60.7K
# Total Submissions: 116.4K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals intervals where intervals[i] =
# [starti, endi], return the minimum number of conference rooms required.
# 
# 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6
# 
# 
#

# @lc code=start
from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        rooms = PriorityQueue()
        rooms.put(intervals[0][-1])
        for i in range(1, n):
            interval = intervals[i]
            room = rooms.get()
            if interval[0] >= room:
                rooms.put(interval[-1])
            else:
                rooms.put(interval[-1])
                rooms.put(room)
        return rooms.qsize()
# @lc code=end

