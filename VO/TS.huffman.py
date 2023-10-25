from collections import *
from heapq import *


class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def encode(s):
    def dfs(node, code):
        if node.val is not None:
            d[node.val] = code
            return
        dfs(node.left, code+'0')
        dfs(node.right, code+'1')
    
    cnt = Counter(s)
    heap = []
    for k in cnt:
        heap.append(Node(k, cnt[k]))
    heapify(heap)
    while len(heap) > 1:
        l = heappop(heap)
        r = heappop(heap)
        n = Node(None, l.freq+r.freq)
        n.left = l
        n.right = r
        heappush(heap, n)
    root = heap[0]
    d = {}
    dfs(root, '')
    ans = ''
    for ch in s:
        ans += d[ch]
    return ans, root

def decode(code, root):
    def dfs(node, i):
        if node.val is not None:
            return node.val, i
        if code[i] == '0':
            return dfs(node.left, i+1)
        else:
            return dfs(node.right, i+1)

    ans = ''
    i = 0
    while i < len(code):
        ch, i = dfs(root, i)
        ans += ch
    return ans


s = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
_, root = encode(s)
print(decode('0100101111', root))  # fcde