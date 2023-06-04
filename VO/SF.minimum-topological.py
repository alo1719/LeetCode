from collections import defaultdict, deque

# Snowflake VOE, Good question!
# TC: O(v+e)  SC: O(v)
class Solution:
    def min_topo(self, time, edges):
        n, g, ans = len(time), defaultdict(list), 0
        in_degree = [0] * n
        for edge in edges:
            g[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
        dq = deque([[i, time[i]] for i in range(n) if in_degree[i] == 0])
        while dq:
            min_time = min([element[1] for element in dq])
            ans += min_time
            new_nodes = []
            for node in list(dq): # important to use list(dq)
                node[1] -= min_time
                if node[1] == 0:
                    dq.remove(node)
                    for to_node in g[node[0]]:
                        in_degree[to_node] -= 1
                        if in_degree[to_node] == 0:
                            new_nodes.append([to_node, time[to_node]])
            dq.extend(new_nodes)
        return ans
    
print(Solution().min_topo([10,5,6], [(2,1)])) # 11
print(Solution().min_topo([12,5,6], [(2,1)])) # 12
print(Solution().min_topo([4,8,4,1,1], [(0,2),(0,3),(1,3),(1,4)])) # 9