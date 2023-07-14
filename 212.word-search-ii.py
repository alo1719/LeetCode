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
# WeRide VOE
# TC: O(mn×3^l), l is the max length of patterns
# SC: O(26l)
from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False
    
    def insert(self, word):
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.is_end = True
    
    # followup, remove word in trie
    def remove(self, word):
        def _remove(node, word, depth):
            if depth == len(word):
                node.is_end = False
                return len(node.children) == 0  # this node has no children
            ch = word[depth]
            if ch not in node.children: return False  # word not in trie
            if _remove(node.children[ch], word, depth+1):
                del node.children[ch]
                return len(node.children) == 0
            return False  #  this node has children, cannot be removed

        _remove(self, word, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, cur_node, cur_str):
            visited[i][j] = True
            if cur_node.is_end and cur_str not in ans:
                ans.add(cur_str)
                # followup, remove word in trie
                trie.remove(cur_str)
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni = i+dx
                nj = j+dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in cur_node.children and not visited[ni][nj]:
                    dfs(ni, nj, cur_node.children[board[ni][nj]], cur_str+board[ni][nj])
                    # backtrack
                    visited[ni][nj] = False

        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        ans = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    visited = [[False]*n for _ in range(m)]
                    dfs(i, j, trie.children[board[i][j]], board[i][j])
        return list(ans)
# @lc code=end

