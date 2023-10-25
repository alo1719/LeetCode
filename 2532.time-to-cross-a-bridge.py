#
# @lc app=leetcode id=2532 lang=python3
#
# [2532] Time to Cross a Bridge
#
# https://leetcode.com/problems/time-to-cross-a-bridge/description/
#
# algorithms
# Hard (51.31%)
# Likes:    98
# Dislikes: 199
# Total Accepted:    3.3K
# Total Submissions: 6.5K
# Testcase Example:  '1\n3\n[[1,1,2,1],[1,1,3,1],[1,1,4,1]]'
#
# There are k workers who want to move n boxes from an old warehouse to a new
# one. You are given the two integers n and k, and a 2D integer array time of
# size k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].
# 
# The warehouses are separated by a river and connected by a bridge. The old
# warehouse is on the right bank of the river, and the new warehouse is on the
# left bank of the river. Initially, all k workers are waiting on the left side
# of the bridge. To move the boxes, the i^th worker (0-indexed) can :
# 
# 
# Cross the bridge from the left bank (new warehouse) to the right bank (old
# warehouse) in leftToRighti minutes.
# Pick a box from the old warehouse and return to the bridge in pickOldi
# minutes. Different workers can pick up their boxes simultaneously.
# Cross the bridge from the right bank (old warehouse) to the left bank (new
# warehouse) in rightToLefti minutes.
# Put the box in the new warehouse and return to the bridge in putNewi minutes.
# Different workers can put their boxes simultaneously.
# 
# 
# A worker i is less efficient than a worker j if either condition is
# met:
# 
# 
# leftToRighti + rightToLefti > leftToRightj + rightToLeftj
# leftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j
# 
# 
# The following rules regulate the movement of the workers through the bridge
# :
# 
# 
# If a worker x reaches the bridge while another worker y is crossing the
# bridge, x waits at their side of the bridge.
# If the bridge is free, the worker waiting on the right side of the bridge
# gets to cross the bridge. If more than one worker is waiting on the right
# side, the one with the lowest efficiency crosses first.
# If the bridge is free and no worker is waiting on the right side, and at
# least one box remains at the old warehouse, the worker on the left side of
# the river gets to cross the bridge. If more than one worker is waiting on the
# left side, the one with the lowest efficiency crosses first.
# 
# 
# Return the instance of time at which the last worker reaches the left bank of
# the river after all n boxes have been put in the new warehouse.
# 
# 
# Example 1:
# 
# 
# Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
# Output: 6
# Explanation: 
# From 0 to 1: worker 2 crosses the bridge from the left bank to the right
# bank.
# From 1 to 2: worker 2 picks up a box from the old warehouse.
# From 2 to 6: worker 2 crosses the bridge from the right bank to the left
# bank.
# From 6 to 7: worker 2 puts a box at the new warehouse.
# The whole process ends after 7 minutes. We return 6 because the problem asks
# for the instance of time at which the last worker reaches the left bank.
# 
# 
# Example 2:
# 
# 
# Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
# Output: 50
# Explanation: 
# From 0  to 10: worker 1 crosses the bridge from the left bank to the right
# bank.
# From 10 to 20: worker 1 picks up a box from the old warehouse.
# From 10 to 11: worker 0 crosses the bridge from the left bank to the right
# bank.
# From 11 to 20: worker 0 picks up a box from the old warehouse.
# From 20 to 30: worker 1 crosses the bridge from the right bank to the left
# bank.
# From 30 to 40: worker 1 puts a box at the new warehouse.
# From 30 to 31: worker 0 crosses the bridge from the right bank to the left
# bank.
# From 31 to 39: worker 0 puts a box at the new warehouse.
# From 39 to 40: worker 0 crosses the bridge from the left bank to the right
# bank.
# From 40 to 49: worker 0 picks up a box from the old warehouse.
# From 49 to 50: worker 0 crosses the bridge from the right bank to the left
# bank.
# From 50 to 58: worker 0 puts a box at the new warehouse.
# The whole process ends after 58 minutes. We return 50 because the problem
# asks for the instance of time at which the last worker reaches the left
# bank.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n, k <= 10^4
# time.length == k
# time[i].length == 4
# 1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda t:t[0]+t[2])  # sort in python is stable
        cur = 0
        workL, waitL, waitR, workR = [], [[-i, 0] for i in range(k-1, -1, -1)], [], []
        while n:
            while workL and workL[0][0] <= cur:  # move from work to wait for L
                p = heappop(workL)
                p[0], p[1] = p[1], p[0]
                heappush(waitL, p)
            while workR and workR[0][0] <= cur:  # move from work to wait for R
                p = heappop(workR)
                p[0], p[1] = p[1], p[0]
                heappush(waitR, p)
            if waitR:  # R to L across the bridge & start to work
                p = heappop(waitR)
                cur += time[-p[0]][2]  # only one worker can use the bridge
                p[1] = p[0]
                p[0] = cur+time[-p[0]][3]
                heappush(workL, p)
            elif waitL:  # L to R across the bridge & start to work
                p = heappop(waitL)
                cur += time[-p[0]][0]
                p[1] = p[0]
                p[0] = cur+time[-p[0]][1]
                heappush(workR, p)
                n -= 1  # send 1 worker to L to R
            elif len(workL) == 0: cur = workR[0][0]  # update cur to make sure some worker is wating
            elif len(workR) == 0: cur = workL[0][0]
            else: cur = min(workL[0][0], workR[0][0])
        while workR:
            t, i = heappop(workR)
            cur = max(t, cur)+time[-i][2]  # does not matter who comes first at this step
        return cur
# @lc code=end

