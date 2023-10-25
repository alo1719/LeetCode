#
# @lc app=leetcode.cn id=2569 lang=python3
#
# [2569] Handling Sum Queries After Update
#
# https://leetcode.cn/problems/handling-sum-queries-after-update/description/
#
# algorithms
# Hard (43.02%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 28.1K
# Testcase Example:  '[1,0,1]\n[0,0,0]\n[[1,1,1],[2,1,0],[3,0,0]]'
#
# You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of
# queries. There are three types of queries:
# 
# 
# For a query of type 1, queries[i] = [1, l, r]. Flip the values from 0 to 1
# and from 1 to 0 in nums1 from index l to index r. Both l and r are
# 0-indexed.
# For a query of type 2, queries[i] = [2, p, 0]. For every index 0 <= i < n,
# set nums2[i] = nums2[i] + nums1[i] * p.
# For a query of type 3, queries[i] = [3, 0, 0]. Find the sum of the elements
# in nums2.
# 
# 
# Return an array containing all the answers to the third type queries.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
# Output: [3]
# Explanation: After the first query nums1 becomes [1,1,1]. After the second
# query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus,
# [3] is returned.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
# Output: [5]
# Explanation: After the first query, nums2 remains [5], so the answer to the
# second query is 5. Thus, [5] is returned.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length,nums2.length <= 10^5
# nums1.length = nums2.length
# 1 <= queries.length <= 10^5
# queries[i].length = 3
# 0 <= l <= r <= nums1.length - 1
# 0 <= p <= 10^6
# 0 <= nums1[i] <= 1
# 0 <= nums2[i] <= 10^9
# 
# 
#

# @lc code=start
class Node:
    def __init__(self, L, R):
        self.left = None
        self.right = None
        self.M = (L+R)//2
        self.L = L
        self.R = R
        # need custimize
        self.cnt1 = 0
        self.lazy_flip = False


class SegmentTree:
    def __init__(self, n):
        self.root = Node(1, n)

    def update(self, L, R, node=None):
        if L > R: return
        if not node: node = self.root
        if node.L >= L and node.R <= R:
            # need custimize
            node.cnt1 = node.R-node.L+1-node.cnt1
            node.lazy_flip = not node.lazy_flip  # flip twice means nothing
            return
        self.pushdown(node)
        if L <= node.M: self.update(L, R, node.left)
        if R > node.M: self.update(L, R, node.right)
        self.pushup(node)

    def query(self, L, R, node=None):
        if L > R: return 0
        if not node: node = self.root
        if node.L >= L and node.R <= R:
            # need custimize
            return node.cnt1
        self.pushdown(node)
        # need custimize
        summ = 0
        if L <= node.M: summ += self.query(L, R, node.left)
        if R > node.M: summ += self.query(L, R, node.right)
        return summ

    def pushup(self, node):
        # need custimize
        node.cnt1 = node.left.cnt1+node.right.cnt1

    def pushdown(self, node):
        if not node.left: node.left = Node(node.L, node.M)
        if not node.right: node.right = Node(node.M+1, node.R)
        # need custimize
        if node.lazy_flip:
            node.left.cnt1 = node.left.R-node.left.L+1-node.left.cnt1
            node.right.cnt1 = node.right.R-node.right.L+1-node.right.cnt1
            node.left.lazy_flip = not node.left.lazy_flip
            node.right.lazy_flip = not node.right.lazy_flip
            node.lazy_flip = False

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        st = SegmentTree(n)
        for i, num in enumerate(nums1):
            if num == 1: st.update(i+1, i+1)
        summ = sum(nums2)
        ans = []
        for op, L, R in queries:
            if op == 1: st.update(L+1, R+1)
            elif op == 2: summ += L*st.query(1, n)
            else: ans.append(summ)
        return ans
# @lc code=end

