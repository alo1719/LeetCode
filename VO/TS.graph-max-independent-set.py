from collections import defaultdict

# TC: O(e*2^v)
def solution(n, edges):
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)
    ans = 0
    for mask in range((1<<n)-1, 0, -1):
        ok = True
        for i in range(n):
            if (mask>>i)&1:
                for j in g[i]:
                    if (mask>>j)&1:
                        ok = False
                        break
            if not ok: break
        if ok:
            ans = max(ans, mask.bit_count())
    return ans

# 最大独立集 Maximum Independent Set
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # f: choose, not choose
        def f(node):
            if not node: return 0, 0
            l_choose, l_not = f(node.left)
            r_choose, r_not = f(node.right)
            choose = node.val+l_not+r_not
            not_choose = max(l_choose, l_not)+max(r_choose, r_not)
            return choose, not_choose
        return max(f(root))

print(solution(3, [[0,1],[0,2]]))  # 2
print(solution(4, [[0,1],[0,2],[0,3],[1,3]]))  # 2
print(solution(4, [[0,1],[0,2],[0,3],[1,3],[1,2]]))  # 2
print(solution(4, [[0,1],[0,2],[0,3],[1,3],[1,2],[2,3]]))  # 1