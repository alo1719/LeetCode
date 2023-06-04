from collections import defaultdict, deque


# TC: O(v+e)  SC: O(v) (ignore the graph)
# like topological sort
class Graph:
    def __init__(self):
        self.g = defaultdict(set)

    def add_edge(self, u, v):
        self.g[u].add(v)
        self.g[v].add(u)

    def k_cores(self, k):
        deleted_nodes = set()
        dq = deque()
        degree = defaultdict(int)
 
        for i in list(self.g):
            degree[i] = len(self.g[i])
            if degree[i] < k:
                dq.append(i)
                deleted_nodes.add(i)
 
        while dq:
            node = dq.popleft()
            for to_node in self.g[node]:
                self.g[to_node].remove(node)
                degree[to_node] -= 1
                degree[node] -= 1
                if degree[to_node] < k and to_node not in deleted_nodes:
                    dq.append(to_node)
                    deleted_nodes.add(to_node)
            del self.g[node]

        return self.g
 

g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(1, 5)
g1.add_edge(2, 3)
g1.add_edge(2, 4)
g1.add_edge(2, 5)
g1.add_edge(2, 6)
g1.add_edge(3, 4)
g1.add_edge(3, 6)
g1.add_edge(3, 7)
g1.add_edge(4, 6)
g1.add_edge(4, 7)
g1.add_edge(5, 6)
g1.add_edge(5, 8)
g1.add_edge(6, 7)
g1.add_edge(6, 8)
print(g1.k_cores(3))

g2 = Graph()
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(0, 3)
print(g2.k_cores(2))

g3 = Graph()
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(0, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 5)
g3.add_edge(2, 6)
g3.add_edge(2, 7)
g3.add_edge(3, 8)
g3.add_edge(3, 9)
g3.add_edge(4, 10)
g3.add_edge(4, 11)
g3.add_edge(5, 12)
g3.add_edge(5, 13)
g3.add_edge(6, 14)
g3.add_edge(6, 15)
g3.add_edge(7, 16)
g3.add_edge(7, 17)
g3.add_edge(8, 18)
g3.add_edge(8, 19)
g3.add_edge(9, 20)
g3.add_edge(9, 21)
print(g3.k_cores(3))