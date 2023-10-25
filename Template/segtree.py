class Node:
    def __init__(self, L, R):
        self.left = None
        self.right = None
        self.M = (L+R)//2
        self.L = L
        self.R = R
        # need custimize
        self.maxx = 0
        self.lazy_add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node(1, 10**9+1)

    def update(self, L, R, V, node=None):
        if L > R: return
        if not node: node = self.root
        if node.L >= L and node.R <= R:
            # need custimize
            node.maxx += V
            node.lazy_add += V
            return
        self.pushdown(node)
        if L <= node.M: self.update(L, R, V, node.left)
        if R > node.M: self.update(L, R, V, node.right)
        self.pushup(node)

    def query(self, L, R, node=None):
        if L > R: return 0
        if not node: node = self.root
        if node.L >= L and node.R <= R:
            # need custimize
            return node.maxx
        self.pushdown(node)
        # need custimize
        maxx = 0
        if L <= node.M: maxx = max(maxx, self.query(L, R, node.left))
        if R > node.M: maxx = max(maxx, self.query(L, R, node.right))
        return maxx

    def pushup(self, node):
        # need custimize
        node.maxx = max(node.left.maxx, node.right.maxx)

    def pushdown(self, node):
        if not node.left: node.left = Node(node.L, node.M)
        if not node.right: node.right = Node(node.M+1, node.R)
        # need custimize
        if node.lazy_add:
            node.left.maxx += node.lazy_add
            node.right.maxx += node.lazy_add
            node.left.lazy_add += node.lazy_add
            node.right.lazy_add += node.lazy_add
            node.lazy_add = 0


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