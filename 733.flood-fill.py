#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.cn/problems/flood-fill/description/
#
# algorithms
# Easy (58.65%)
# Likes:    410
# Dislikes: 0
# Total Accepted:    146.8K
# Total Submissions: 250.2K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
# 
# You are also given three integers sr, sc, and color. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
# 
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
# 
# Return the modified image after performing the flood fill.
# 
# 
# Example 1:
# 
# 
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
# 
# 
# Example 2:
# 
# 
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made
# to the image.
# 
# 
# 
# Constraints:
# 
# 
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
# 
# 
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            nonlocal color, color_ori, m, n
            if i >= m or i < 0 or j >= n or j < 0:
                return
            if image[i][j] == color_ori:
                image[i][j] = color
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        color_ori = image[sr][sc]
        m, n = len(image), len(image[0])
        if color_ori != color: dfs(sr, sc)
        return image
# @lc code=end

