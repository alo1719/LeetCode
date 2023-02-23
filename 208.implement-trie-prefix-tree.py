#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.cn/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (72.02%)
# Likes:    1379
# Dislikes: 0
# Total Accepted:    246.8K
# Total Submissions: 342.7K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
# 
# Implement the Trie class:
# 
# 
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# 
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
# 
# 
#

# @lc code=start
# Tool, 26-children tree
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        current_node = self
        for char in word:
            char_offset = ord(char)-ord("a")
            if not current_node.children[char_offset]:
                current_node.children[char_offset] = Trie() # new node
            current_node = current_node.children[char_offset]
        current_node.isEnd = True

    def search(self, word: str) -> bool:
        search_result_node = self.searchPrefix(word)
        return search_result_node is not None and search_result_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
    
    def searchPrefix(self, prefix):
        current_node = self
        for char in prefix:
            char_offset = ord(char)-ord("a")
            if not current_node.children[char_offset]:
                return None
            current_node = current_node.children[char_offset]
        return current_node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

