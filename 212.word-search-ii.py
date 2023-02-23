#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.cn/problems/word-search-ii/description/
#
# algorithms
# Hard (44.40%)
# Likes:    738
# Dislikes: 0
# Total Accepted:    87.9K
# Total Submissions: 198.1K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# 
# 
#

# @lc code=start
# Snowflake VOE, Trie, Good question!
from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False
    
    def insert(self, word):
        current_node = self
        for ch in word:
            current_node = current_node.children[ch]
        current_node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, now_node, now_str):
            nonlocal n, m
            visited[i][j] = True
            if now_node.is_end and now_str not in ans: # can use a set to optimize
                ans.append(now_str)
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                newi = i + dx
                newj = j + dy
                if 0<=newi<n and 0<=newj<m and board[newi][newj] in now_node.children and not visited[newi][newj]:
                    dfs(newi, newj, now_node.children[board[newi][newj]], now_str+board[newi][newj])
                    # backtrack
                    visited[newi][newj] = False

        trie = Trie()
        for word in words:
            trie.insert(word)
        n, m = len(board), len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = []
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.children:
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    dfs(i, j, trie.children[board[i][j]], board[i][j])
        return ans
# @lc code=end

