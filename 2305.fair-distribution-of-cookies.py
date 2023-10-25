#
# @lc app=leetcode id=2305 lang=python3
#
# [2305] Fair Distribution of Cookies
#
# https://leetcode.com/problems/fair-distribution-of-cookies/description/
#
# algorithms
# Medium (61.72%)
# Likes:    1028
# Dislikes: 51
# Total Accepted:    29.1K
# Total Submissions: 45.9K
# Testcase Example:  '[8,15,10,20,8]\n2'
#
# You are given an integer array cookies, where cookies[i] denotes the number
# of cookies in the i^th bag. You are also given an integer k that denotes the
# number of children to distribute all the bags of cookies to. All the cookies
# in the same bag must go to the same child and cannot be split up.
# 
# The unfairness of a distribution is defined as the maximum total cookies
# obtained by a single child in the distribution.
# 
# Return the minimum unfairness of all distributions.
# 
# 
# Example 1:
# 
# 
# Input: cookies = [8,15,10,20,8], k = 2
# Output: 31
# Explanation: One optimal distribution is [8,15,8] and [10,20]
# - The 1^st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31
# cookies.
# - The 2^nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
# The unfairness of the distribution is max(31,30) = 31.
# It can be shown that there is no distribution with an unfairness less than
# 31.
# 
# 
# Example 2:
# 
# 
# Input: cookies = [6,1,3,2,2,4,1,2], k = 3
# Output: 7
# Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
# - The 1^st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
# - The 2^nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
# - The 3^rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
# The unfairness of the distribution is max(7,7,7) = 7.
# It can be shown that there is no distribution with an unfairness less than
# 7.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= cookies.length <= 8
# 1 <= cookies[i] <= 10^5
# 2 <= k <= cookies.length
# 
# 
#

# @lc code=start
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        @cache
        def f(i, mask):
            if i == n and not mask: return 0
            ans = inf
            while mask:
                new_mask = mask&(mask-1) # subset
                summ = 0
                for j in range(n):
                    if new_mask>>j&1: summ += cookies[j]
                ans = min(ans, max(f(i+1, new_mask), summ))
            return ans
        # 111000 6 cookies n
        n = len(cookies)
        return f(0, (1<<n)-1)
# @lc code=end

