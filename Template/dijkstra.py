from collections import defaultdict
from queue import PriorityQueue

# TC: O((v+e)logv)  SC: O(v) (ignore the graph)
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

# TC: O(ve)
def bellman_ford(edges, start, n):
    g = defaultdict(list)
    for edge in edges:
        g[edge[0]].append((edge[1], edge[2]))
    dis = [float('inf')]*n
    dis[start] = 0
    fromm = [None]*n
    for i in range(n-1):
        for edge in edges:
            if dis[edge[1]] > dis[edge[0]]+edge[2]:
                dis[edge[1]] = dis[edge[0]]+edge[2]
                fromm[edge[1]] = edge[0]
    for edge in edges:
        if dis[edge[1]] > dis[edge[0]]+edge[2]:
            print('negative cycle')
            return
    return dis, fromm

print(dijkstra([(0,1,1),(1,2,2),(2,3,3),(3,4,1),(4,5,2),(5,3,1),(0,4,99)], 0, 6))
print(bellman_ford([(0,1,1),(1,2,2),(2,3,3),(3,4,1),(4,5,2),(5,3,1),(0,4,99)], 0, 6))
print(bellman_ford([(0,1,1),(1,2,2),(2,0,-4)], 0, 3))
