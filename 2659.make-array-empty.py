#
# @lc app=leetcode.cn id=2659 lang=python3
#
# [2659] Make Array Empty
#
# https://leetcode.cn/problems/make-array-empty/description/
#
# algorithms
# Hard (39.27%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 5.7K
# Testcase Example:  '[3,4,-1]'
#
# You are given an integer array nums containing distinct numbers, and you can
# perform the following operations until the array is empty:
# 
# 
# If the first element has the smallest value, remove it
# Otherwise, put the first element at the end of the array.
# 
# 
# Return an integer denoting the number of operations it takes to make nums
# empty.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,4,-1]
# Output: 5
# 
# 
# 
# 
# 
# Operation
# Array
# 
# 
# 
# 
# 1
# [4, -1, 3]
# 
# 
# 2
# [-1, 3, 4]
# 
# 
# 3
# [3, 4]
# 
# 
# 4
# [4]
# 
# 
# 5
# []
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,4,3]
# Output: 5
# 
# 
# 
# 
# 
# Operation
# Array
# 
# 
# 
# 
# 1
# [2, 4, 3]
# 
# 
# 2
# [4, 3]
# 
# 
# 3
# [3, 4]
# 
# 
# 4
# [4]
# 
# 
# 5
# []
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3]
# Output: 3
# 
# 
# 
# 
# 
# Operation
# Array
# 
# 
# 
# 
# 1
# [2, 3]
# 
# 
# 2
# [3]
# 
# 
# 3
# []
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# All values in nums are distinct.
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
            if l&1:
                al = self.f(al, self.X[l])
                l += 1
            if r&1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

# TC: O(nlogn)  SC: O(n)
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        ans = n = len(nums)
        st = SegmentTree(n, 0, lambda x, y:x+y)
        pre = 0
        ids = sorted(range(n), key=lambda x:nums[x])
        for i in ids:
            if pre <= i:
                ans += i-pre-st.getrange(pre, i)
            else:
                ans += n-(pre-i)-st.getrange(pre, n-1)-st.getrange(0, i)
            st.update(i, 1)
            pre = i
        return ans
# @lc code=end

