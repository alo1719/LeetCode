#
# @lc app=leetcode.cn id=2736 lang=python3
#
# [2736] Maximum Sum Queries
#
# https://leetcode.cn/problems/maximum-sum-queries/description/
#
# algorithms
# Hard (39.98%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 6K
# Testcase Example:  '[4,3,1,2]\n[2,4,9,5]\n[[4,1],[1,3],[2,5]]'
#
# You are given two 0-indexed integer arrays nums1 and nums2, each of length n,
# and a 1-indexed 2D array queries where queries[i] = [xi, yi].
# 
# For the i^th query, find the maximum value of nums1[j] + nums2[j] among all
# indices j (0 <= j < n), where nums1[j] >= xi and nums2[j] >= yi, or -1 if
# there is no j satisfying the constraints.
# 
# Return an array answer where answer[i] is the answer to the i^th query.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
# Output: [6,10,7]
# Explanation: 
# For the 1st query xi = 4 and yi = 1, we can select index j = 0 since nums1[j]
# >= 4 and nums2[j] >= 1. The sum nums1[j] + nums2[j] is 6, and we can show
# that 6 is the maximum we can obtain.
# 
# For the 2nd query xi = 1 and yi = 3, we can select index j = 2 since nums1[j]
# >= 1 and nums2[j] >= 3. The sum nums1[j] + nums2[j] is 10, and we can show
# that 10 is the maximum we can obtain. 
# 
# For the 3rd query xi = 2 and yi = 5, we can select index j = 3 since nums1[j]
# >= 2 and nums2[j] >= 5. The sum nums1[j] + nums2[j] is 7, and we can show
# that 7 is the maximum we can obtain.
# 
# Therefore, we return [6,10,7].
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
# Output: [9,9,9]
# Explanation: For this example, we can use index j = 2 for all the queries
# since it satisfies the constraints for each query.
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]
# Output: [-1]
# Explanation: There is one query in this example with xi = 3 and yi = 3. For
# every index, j, either nums1[j] < xi or nums2[j] < yi. Hence, there is no
# solution. 
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == nums2.length 
# n == nums1.length 
# 1 <= n <= 10^5
# 1 <= nums1[i], nums2[i] <= 10^9 
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# xi == queries[i][1]
# yi == queries[i][2]
# 1 <= xi, yi <= 10^9
# 
# 
#

# @lc code=start
class SegmentTree():
    def __init__(self, n, unitX, f):
        self.f = f  # (X, X) -> X
        self.unitX = unitX
        self.n = n
        self.n = 1<<(self.n-1).bit_length()
        self.X = [unitX]*(self.n*2)  # 0-indexed

    def update(self, i, x):
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1

    def getvalue(self, i):
        return self.X[i+self.n]

    def getrange(self, l, r):
        l += self.n
        r += self.n+1  # [l, r]
        al = self.unitX
        ar = self.unitX
        while l < r:
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums1), len(queries)
        queries = sorted(zip(queries, range(q)))
        sn1 = sorted(zip(nums1, range(n)))
        sn2 = [(nums2[i], i) for i in range(n)]
        sn2 += [(queries[i][0][1], -1) for i in range(q)]
        sn2.sort()
        di, dv = [0]*n, {}
        m = len(sn2)
        for i in range(m):
            if sn2[i][1] != -1:
                di[sn2[i][1]] = i  # map original pos to i
            if sn2[i][0] not in dv:
                dv[sn2[i][0]] = i  # map value to i
        st = SegmentTree(m, -1, max)
        for i in range(n):
            st.update(di[i], nums1[i]+nums2[i])
        
        pos = 0
        ans = [0]*q
        for (x, y), i in queries:
            while pos < n and sn1[pos][0] < x:
                st.update(di[sn1[pos][1]], -1)
                pos += 1
            ans[i] = st.getrange(dv[y], m-1)
        return ans
# @lc code=end

