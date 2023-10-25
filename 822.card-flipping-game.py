#
# @lc app=leetcode.cn id=822 lang=python3
#
# [822] Card Flipping Game
#
# https://leetcode.cn/problems/card-flipping-game/description/
#
# algorithms
# Medium (51.69%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 22K
# Testcase Example:  '[1,2,4,4,7]\n[1,3,4,1,3]'
#
# You are given two 0-indexed integer arrays fronts and backs of length n,
# where the i^th card has the positive integer fronts[i] printed on the front
# and backs[i] printed on the back. Initially, each card is placed on a table
# such that the front number is facing up and the other is facing down. You may
# flip over any number of cards (possibly zero).
# 
# After flipping the cards, an integer is considered good if it is facing down
# on some card and not facing up on any card.
# 
# Return the minimum possible good integer after flipping the cards. If there
# are no good integers, return 0.
# 
# 
# Example 1:
# 
# 
# Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
# Output: 2
# Explanation:
# If we flip the second card, the face up numbers are [1,3,4,4,7] and the face
# down are [1,2,4,1,3].
# 2 is the minimum good integer as it appears facing down but not facing up.
# It can be shown that 2 is the minimum possible good integer obtainable after
# flipping some cards.
# 
# 
# Example 2:
# 
# 
# Input: fronts = [1], backs = [1]
# Output: 0
# Explanation:
# There are no good integers no matter how we flip the cards, so we return
# 0.
# 
# 
# 
# Constraints:
# 
# 
# n == fronts.length == backs.length
# 1 <= n <= 1000
# 1 <= fronts[i], backs[i] <= 2000
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        sett = set()
        n = len(fronts)
        for i in range(n):
            if fronts[i] == backs[i]:
                sett.add(fronts[i])
        return min([i for i in fronts+backs if i not in sett] or [0])
# @lc code=end

