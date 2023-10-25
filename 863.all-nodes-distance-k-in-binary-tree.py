#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (62.74%)
# Likes:    9833
# Dislikes: 190
# Total Accepted:    362.3K
# Total Submissions: 567.1K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# Given the root of a binary tree, the value of a target node target, and an
# integer k, return an array of the values of all nodes that have a distance k
# from the target node.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value
# 5) have values 7, 4, and 1.
# 
# 
# Example 2:
# 
# 
# Input: root = [1], target = 1, k = 3
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node):
            if not node: return
            if node.left:
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)
                dfs(node.right)
        g = defaultdict(list)
        dfs(root)
        ans = []
        v = set([target.val])
        dq = deque([target.val])
        while dq:
            lenn = len(dq)
            if not k: return list(dq)
            for _ in range(lenn):
                node = dq.popleft()
                for to_node in g[node]:
                    if to_node not in v:
                        dq.append(to_node)
                        v.add(to_node)
            k -= 1
        return []
# @lc code=end

