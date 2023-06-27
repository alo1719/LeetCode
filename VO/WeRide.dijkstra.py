from collections import defaultdict
from queue import PriorityQueue

# TC: O(v+elogv)  SC: O(v) (ignore the graph)
def dijkstra(edges, start, n):
    g = defaultdict(list)
    for edge in edges:
        g[edge[0]].append((edge[1], edge[2]))
    queue = PriorityQueue()
    queue.put((0, start))
    dis = [float('inf')]*n
    dis[start] = 0
    fromm = [None]*n
    while not queue.empty():
        cur_dis, node = queue.get()
        for to_node, weight in g[node]:
            if dis[to_node] > cur_dis+weight:
                dis[to_node] = cur_dis+weight
                fromm[to_node] = node
                queue.put((dis[to_node], to_node))
    return dis, fromm

print(dijkstra([(0,1,1),(1,2,2),(2,3,3),(3,4,1),(4,5,2),(5,3,1),(0,4,99)], 0, 6))
