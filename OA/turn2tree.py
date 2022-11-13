from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.childrens = []
        self.isLeaf = True if "." in val else False

def turn2tree(ss: List[str]) -> TreeNode:
    root = TreeNode("/")
    for s in ss:
        path = s.split('/')
        print(path)
        now = root
        for p in path:
            if p == "":
                continue
            index = -1
            for i, c in enumerate(now.childrens):
                if c.val == p:
                    print("find", p)
                    index = i
                    break
            if index == -1:
                now.childrens.append(TreeNode(p))
                print("now", now.val, "add", p)
            now = now.childrens[index]
    return root

input = ["/a/b.txt","/b/c.txt","/b/d.txt","/c/d.txt","/c/e.txt"]
rst = turn2tree(input)
for i in rst.childrens:
    print(i.val)
    for j in i.childrens:
        print("/:",j.val)