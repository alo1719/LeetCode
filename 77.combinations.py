#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.08%)
# Likes:    1441
# Dislikes: 0
# Total Accepted:    564.8K
# Total Submissions: 732.7K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # choose or not choose, TC: O(k*C(n, k)), SC: O(n)
        def f(i):
            if n-i < k-len(path): return  # no enough numbers
            if len(path) == k:
                ans.append(path[:])
                return
            f(i+1)  # not choose
            path.append(i+1)
            f(i+1)  # choose
            path.pop()
        ans = []
        path = []
        f(0)
        return ans
# @lc code=end

