#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#
# https://leetcode.cn/problems/best-team-with-no-conflicts/description/
#
# algorithms
# Medium (53.66%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 47.4K
# Testcase Example:  '[1,3,5,10,15]\n[1,2,3,4,5]'
#
# You are the manager of a basketball team. For the upcoming tournament, you
# want to choose the team with the highest overall score. The score of the team
# is the sum of scores of all the players in the team.
# 
# However, the basketball team is not allowed to have conflicts. A conflict
# exists if a younger player has a strictly higher score than an older player.
# A conflict does not occur between players of the same age.
# 
# Given two lists, scores and ages, where each scores[i] and ages[i] represents
# the score and age of the i^th player, respectively, return the highest
# overall score of all possible basketball teams.
# 
# 
# Example 1:
# 
# 
# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.
# 
# 
# Example 2:
# 
# 
# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are
# allowed to choose multiple people of the same age.
# 
# 
# Example 3:
# 
# 
# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players. 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 10^6
# 1 <= ages[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        s = scores
        a = ages
        n = len(s)
        z = sorted(zip(a, s))
        f = [z[0][1]]+[0]*(n-1)
        for i in range(1, n):
            # f[i] = f[i-1]
            for j in range(i-1, -1, -1):
                if z[j][0] == z[i][0] or (z[j][0] < z[i][0] and z[j][1] <= z[i][1]):
                    f[i] = max(f[i], f[j])
            f[i] += z[i][1]
            # print(f)
        return max(f)
# @lc code=end

