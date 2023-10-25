#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Medium (37.29%)
# Likes:    351
# Dislikes: 20
# Total Accepted:    1.4M
# Total Submissions: 3.8M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#

# @lc code=start
# TC: O(n+m)  SC: O(n)
class Solution:
    # Rabbin-Karp
    def strStr(self, haystack: str, needle: str) -> int:
        prime = 31
        mod = 10**9+9
        haystack_len, needle_len = len(haystack), len(needle)
        pow = [1]*max(haystack_len, needle_len)
        for i in range(1, len(pow)):
            pow[i] = (pow[i-1]*prime)%mod
        needle_hash = 0
        haystack_hash = [0]*haystack_len
        for i in range(needle_len):
            needle_hash = (needle_hash+(ord(needle[i])-ord('a')+1)*pow[i])%mod
        for i in range(haystack_len):
            last_hash_value = 0 if i == 0 else haystack_hash[i-1]
            haystack_hash[i] = (last_hash_value+(ord(haystack[i])-ord('a')+1)*pow[i])%mod
        for i in range(haystack_len-needle_len+1):
            last_hash_value = 0 if i == 0 else haystack_hash[i-1]
            # hash of [i, j] is (hash[j] - hash[i-1])
            cur_hash = (haystack_hash[i+needle_len-1]-last_hash_value+mod)%mod
            # shift pattern hash
            if (cur_hash == needle_hash*pow[i]%mod):
                return i
        return -1
# @lc code=end
