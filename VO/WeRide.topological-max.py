from collections import defaultdict, deque

# TC: O(v+e)  SC: O(v) (ignore the graph)
def topological_max(paths, value):
    g = defaultdict(list)
    n = len(value)
    degree = [0] * n
    for path in paths:
        g[path[0]].append(path[1])
        degree[path[1]] += 1
    dq = deque()
    max_from = [i for i in range(n)]
    for i in range(n):
        if degree[i] == 0:
            dq.append(i)
            max_from[i] = i
    while dq:
        node = dq.popleft()
        for to_node in g[node]:
            degree[to_node] -= 1
            if value[max_from[node]] > value[max_from[to_node]]:
                max_from[to_node] = max_from[node]
            if degree[to_node] == 0:
                dq.append(to_node)
    return [value[max_from[i]] for i in range(n)]

print(topological_max([[0,1],[1,3],[2,1],[4,2]], [5,2,1,4,8])) # 5,8,8,8,8
