#
# @lc app=leetcode.cn id=920 lang=python3
#
# [920] Number of Music Playlists
#
# https://leetcode.cn/problems/number-of-music-playlists/description/
#
# algorithms
# Hard (52.29%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 6.7K
# Testcase Example:  '3\n3\n1'
#
# Your music player contains n different songs. You want to listen to goal
# songs (not necessarily different) during your trip. To avoid boredom, you
# will create a playlist so that:
# 
# 
# Every song is played at least once.
# A song can only be played again only if k other songs have been played.
# 
# 
# Given n, goal, and k, return the number of possible playlists that you can
# create. Since the answer can be very large, return it modulo 10^9 + 7.
# 
# Example 1:
# 
# 
# Input: n = 3, goal = 3, k = 1
# Output: 6
# Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3],
# [2, 3, 1], [3, 1, 2], and [3, 2, 1].
# 
# 
# Example 2:
# 
# 
# Input: n = 2, goal = 3, k = 0
# Output: 6
# Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1],
# [2, 2, 1], [2, 1, 2], and [1, 2, 2].
# 
# 
# Example 3:
# 
# 
# Input: n = 2, goal = 3, k = 1
# Output: 2
# Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= k < n <= goal <= 100
# 
# 
#

# @lc code=start
# TC: O(goal*n)  SC: O(goal*n)
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # f[i][j]: i songs, j distinct songs
        # f[i][j] = f[i-1][j-1]*(n-j+1)+f[i-1][j]*(j-k) if j-k > 0
        #               different         same
        @cache
        def f(i, j):
            if i == 1: return n*int(j == 1)
            diff = f(i-1, j-1)*(n-j+1)
            same = max(f(i-1, j)*(j-k), 0)
            return (diff+same)%MOD
        MOD = 10**9+7
        return f(goal, n)
# @lc code=end

