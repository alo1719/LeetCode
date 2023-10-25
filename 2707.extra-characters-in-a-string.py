#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#
# https://leetcode.com/problems/extra-characters-in-a-string/description/
#
# algorithms
# Medium (32.81%)
# Likes:    297
# Dislikes: 25
# Total Accepted:    11.3K
# Total Submissions: 33.9K
# Testcase Example:  '"leetscode"\n["leet","code","leetcode"]'
#
# You are given a 0-indexed string s and a dictionary of words dictionary. You
# have to break s into one or more non-overlapping substrings such that each
# substring is present in dictionary. There may be some extra characters in s
# which are not present in any of the substrings.
# 
# Return the minimum number of extra characters left over if you break up s
# optimally.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and
# "code" from index 5 to 8. There is only 1 unused character (at index 4), so
# we return 1.
# 
# 
# 
# Example 2:
# 
# 
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and
# "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in
# any substring and thus are considered as extra characters. Hence, we return
# 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters
# dictionary contains distinct words
# 
# 
#

# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        sett = set(dictionary)
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(n):
            for j in range(i+1):
                if s[j:i+1] in sett:
                    dp[i+1] = min(dp[i+1], dp[j])
                dp[i+1] = min(dp[i+1], dp[i]+1)
        return dp[-1]

# @lc code=end

