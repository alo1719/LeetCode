class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]  # array DSU
        # self.root = defaultdict(int)  # dict DSU
        # optional attributes
        self.cnt = [1 for _ in range(n)]  # array format, can customize
        self.weight = defaultdict(float)  # dict format, can customize
    
    def add(self, x):  # optional, for dict DSU
        if x not in self.root:
            self.root[x] = x
            # optional
            self.weight[x] = 1
            self.cnt[x] = 1
    
    def find(self, x):
        if self.root[x] == x: return x
        old_root = self.root[x]  # optional, for weighted DSU
        self.root[x] = self.find(self.root[x])
        self.weight[x] *= self.weight[old_root]  # optional
        return self.root[x]
    
    def union(self, a, b, v=1):  # v for weighted DSU
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b
        self.weight[root_a] = v/self.weight[a]*self.weight[b]  # optional
        self.cnt[root_b] += self.cnt[root_a]  # optional
