# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def help(root):
            nonlocal k
            nonlocal ans
            # go to the left most
            if root.left:
                help(root.left)
            k-=1
            if k==0:
                ans=root.val
            if root.right:
                help(root.right)
            
        ans=-1
        help(root)
        return ans