from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Snowflake VOE
# TC: O(n)  SC: O(n)
def isPerfectTree(root: Optional[TreeNode]) -> bool:
    dq = deque([root])
    num_per_level = 1
    while dq:
        lenn = len(dq)
        if lenn != num_per_level: return False
        for _ in range(lenn):
            node = dq.popleft()
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
        num_per_level *= 2
    return True

# TC: O(n)  SC: O(n)
def fill2PerfectTree(root):
    if not root: return root
    existing_num = 0
    dq = deque([root])
    # calc existing_num
    while dq:
        lenn = len(dq)
        existing_num += lenn
        for _ in range(lenn):
            node = dq.popleft()
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
    # level by level
    dq = deque([root])
    perfect_fill_num = 0
    perfect_del_num = 0
    min_num = float('inf')
    optimal_level = 0
    num_per_level = 1
    current_num = 0
    current_level = 0
    while dq:
        lenn = len(dq)
        current_num += lenn
        current_level += 1
        perfect_fill_num += num_per_level - lenn
        perfect_del_num = existing_num - current_num
        optimal_level += 1
        if perfect_del_num + perfect_fill_num < min_num:
            min_num = perfect_del_num + perfect_fill_num
            optimal_level = current_level
        for _ in range(lenn):
            node = dq.popleft()
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
        num_per_level *= 2
    # fill & del
    dq = deque([root])
    current_level = 0
    while dq:
        lenn = len(dq)
        current_level += 1
        for _ in range(lenn):
            node = dq.popleft()
            if current_level < optimal_level:
                if not node.left: node.left = TreeNode()
                if not node.right: node.right = TreeNode()
                dq.append(node.left)
                dq.append(node.right)
            if current_level == optimal_level:
                node.left = None
                node.right = None
    return root, min_num


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(isPerfectTree(root)) # True
print(fill2PerfectTree(root)) # 0
print(isPerfectTree(root)) # True
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
print(isPerfectTree(root)) # Flase
print(fill2PerfectTree(root)) # 1
print(isPerfectTree(root)) # True
root = TreeNode(1, TreeNode(2, TreeNode(4)))
print(isPerfectTree(root)) # Flase
print(fill2PerfectTree(root)) # 2
print(isPerfectTree(root)) # True