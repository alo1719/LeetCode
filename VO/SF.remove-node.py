# Snowflake VOE
class Solution:
    def remove_node(self, list, node):
        n = len(list)
        removed_set = set()
        new_list = []
        for i in range(n):
            if list[i][0] == node or list[i][1] in removed_set:
                removed_set.add(list[i][0])
                continue
            else:
                new_list.append(list[i])
        m = len(new_list)
        for i in range(m):
            if new_list[i][0] != i:
                for j in range(i, m):
                    if new_list[j][1] == new_list[i][0]:
                        new_list[j] = (new_list[j][0], i)
                new_list[i] = (i, new_list[i][1])
        print(new_list)
    
Solution().remove_node([(0,0),(1,1),(2,2),(3,3)], 1) # [(0,0),(1,1),(2,2)]
Solution().remove_node([(0,0),(1,1),(2,1),(3,1)], 1) # [(0,0)]
Solution().remove_node([(0,0),(1,0),(2,0),(3,2),(4,4),(5,3),(6,4)], 2) # [(0,0),(1,0),(2,2),(3,2)]