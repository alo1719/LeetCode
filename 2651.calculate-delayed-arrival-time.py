#
# @lc app=leetcode id=2651 lang=python3
#
# [2651] Calculate Delayed Arrival Time
#
# https://leetcode.com/problems/calculate-delayed-arrival-time/description/
#
# algorithms
# Easy (82.79%)
# Likes:    102
# Dislikes: 20
# Total Accepted:    24.4K
# Total Submissions: 29.5K
# Testcase Example:  '15\n5'
#
# You are given a positive integer arrivalTime denoting the arrival time of a
# train in hours, and another positive integer delayedTime denoting the amount
# of delay in hours.
# 
# Return the time when the train will arrive at the station.
# 
# Note that the time in this problem is in 24-hours format.
# 
# 
# Example 1:
# 
# 
# Input: arrivalTime = 15, delayedTime = 5 
# Output: 20 
# Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5
# hours. Now it will reach at 15+5 = 20 (20:00 hours).
# 
# 
# Example 2:
# 
# 
# Input: arrivalTime = 13, delayedTime = 11
# Output: 0
# Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11
# hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours
# format so return 0).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arrivaltime < 24
# 1 <= delayedTime <= 24
# 
# 
#

# @lc code=start
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24
# @lc code=end

