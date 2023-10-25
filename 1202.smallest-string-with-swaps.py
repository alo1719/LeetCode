#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#
# https://leetcode.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (57.80%)
# Likes:    3386
# Dislikes: 120
# Total Accepted:    100.6K
# Total Submissions: 174.1K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# You are given a string s, and an array of pairs of indices in the string
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# 
# You can swap the characters at any pair of indices in the given pairs any
# number of times.
# 
# Return the lexicographically smallest string that s can be changed to after
# using the swaps.
# 
# 
# Example 1:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# 
# 
# Example 2:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# 
# Example 3:
# 
# 
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
# 
# 
#

# @lc code=start
class UFS:
  def __init__(self, m):
    self.root = [x for x in range(m)]
  
  def find(self, x):
    if x == self.root[x]: return x
    self.root[x] = self.find(self.root[x])
    return self.root[x]
  
  def union(self, a, b):
    ra, rb = self.find(a), self.find(b)
    self.root[ra] = rb

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(pairs)
        m = len(s)
        ufs = UFS(m)
        for i in range(n):
            node1, node2 = pairs[i]
            ufs.union(node1, node2)
        dictt = defaultdict(lambda: defaultdict(int))
        for i in range(m):
            dictt[ufs.find(i)][s[i]] += 1
        ans = ""
        for i in range(m):
            tmp = sorted(list(dictt[ufs.find(i)]))[0]
            ans += tmp
            dictt[ufs.find(i)][tmp] -= 1
            if dictt[ufs.find(i)][tmp] == 0:
                del dictt[ufs.find(i)][tmp]
        return ans
# @lc code=end

