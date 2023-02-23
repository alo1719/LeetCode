from collections import defaultdict, deque

# Snowflake VOE, Good question!
class Solution:
    def min_topo(self, time, pres):
        n = len(time)
        edges = defaultdict(list)
        node_in_num = [0] * n
        for pre in pres:
            edges[pre[0]].append(pre[1])
            node_in_num[pre[1]] += 1
        dq = deque([[i, time[i]] for i in range(n) if node_in_num[i] == 0])
        ans = 0
        while dq:
            print(dq)
            min_time = min([element[1] for element in dq])
            ans += min_time
            new_nodes = []
            for dq_node in list(dq): # important to use list(dq)
                dq_node[1] -= min_time
                if dq_node[1] == 0:
                    dq.remove(dq_node)
                    for to_node in edges[dq_node[0]]:
                        node_in_num[to_node] -= 1
                        if node_in_num[to_node] == 0:
                            new_nodes.append([to_node, time[to_node]])
            dq.extend(new_nodes)
        
        print(ans)
    
Solution().min_topo([10,5,6], [(2,1)]) # 11
Solution().min_topo([12,5,6], [(2,1)]) # 12
Solution().min_topo([4,8,4,1,1], [(0,2),(0,3),(1,3),(1,4)]) # 9