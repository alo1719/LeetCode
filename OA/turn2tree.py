from collections import defaultdict


class TreeNode:
    def __init__(self):
        self.childrens = defaultdict(TreeNode)

# TC: O(n)  SC: O(n), n is the total number of subpaths
def turn2tree(strs) -> TreeNode:
    root = TreeNode()
    for str in strs:
        path = str.split('/')
        cur = root
        for p in path:
            if not p: continue
            cur = cur.childrens[p]
    return root

input = ["/a/b.txt","/b/c.txt","/b/d.txt","/c/d.txt","/c/e.txt"]
ans = turn2tree(input)
for i in ans.childrens:
    print(i)
    for j in ans.childrens[i].childrens:
        print("|-", j)