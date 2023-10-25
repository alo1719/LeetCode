#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
#
# algorithms
# Medium (61.47%)
# Likes:    1640
# Dislikes: 44
# Total Accepted:    38.3K
# Total Submissions: 62.1K
# Testcase Example:  '[1,2,3,null,4]\n3'
#
# You are given the root of a binary tree and an integer distance. A pair of
# two different leaf nodes of a binary tree is said to be good if the length of
# the shortest path between them is less than or equal to distance.
# 
# Return the number of good leaf node pairs in the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the
# shortest path between them is 3. This is the only good pair.
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The
# pair [4,6] is not good because the length of ther shortest path between them
# is 4.
# 
# 
# Example 3:
# 
# 
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 2^10].
# 1 <= Node.val <= 100
# 1 <= distance <= 10
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC: O(n*distance^2)  SC: O(n*distance^2)
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # return: (at depth i, #leaves (array), #pairs)
        def dfs(node, distance):
            dp = [0]*(distance+1)  # at depth i, #leaves
            if not node.left and not node.right:
                dp[0] = 1
                return dp, 0
            ldp, rdp = [0]*(distance+1), [0]*(distance+1)
            lcnt = rcnt = 0

            if node.left:
                ldp, lcnt = dfs(node.left, distance)
            if node.right:
                rdp, rcnt = dfs(node.right, distance)
            
            for i in range(distance):
                dp[i+1] += ldp[i]+rdp[i]
            
            cnt = 0  # use current node as parent, count #pairs
            for i in range(distance+1):
                for j in range(distance-i-1):
                    cnt += ldp[i]*rdp[j]
            return dp, cnt+lcnt+rcnt
        
        return dfs(root, distance)[1]
# @lc code=end

