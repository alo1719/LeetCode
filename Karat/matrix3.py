# TC: O(number of all possible moves)
# SC: O(n * longest move)
def validMoves(start, end):
    def dfs(now):
        if str(now) == str(end):
            return True
        for i in range(n):
            if now[i] == 'R':
                if i+1 < n and now[i+1] == '_':
                    now[i], now[i+1] = '_', 'R'
                    ans.append(now.copy())
                    if str(now) not in vis:
                        vis.add(str(now))
                        if dfs(now): return True
                    now[i], now[i+1] = 'R', '_'
                    ans.pop()
                if i+2 < n and now[i+2] == '_' and now[i+1] != 'R':
                    now[i], now[i+2] = '_', 'R'
                    ans.append(now.copy())
                    if str(now) not in vis:
                        vis.add(str(now))
                        if dfs(now): return True
                    now[i], now[i+2] = 'R', '_'
                    ans.pop()
            if now[i] == 'B':
                if i-1 >= 0 and now[i-1] == '_':
                    now[i-1], now[i] = 'B', '_'
                    ans.append(now.copy())
                    if str(now) not in vis:
                        vis.add(str(now))
                        if dfs(now): return True
                    now[i-1], now[i] = '_', 'B'
                    ans.pop()
                if i-2 >= 0 and now[i-2] == '_' and now[i-1] != 'B':
                    now[i-2], now[i] = 'B', '_'
                    ans.append(now.copy())
                    if str(now) not in vis:
                        vis.add(str(now))
                        if dfs(now): return True
                    now[i-2], now[i] = '_', 'B'
                    ans.pop()

    vis, n = set(), len(start)
    ans = [start.copy()]
    if not dfs(start):
        print(None)
    else:
        print(ans)

start = ["R", "_", "B", "B"]
end = ["B", "_", "B", "R"]
# [['R', '_', 'B', 'B'], ['_', 'R', 'B', 'B'], ['B', 'R', '_', 'B'], ['B', 'R', 'B', '_'], ['B', '_', 'B', 'R']]
validMoves(start, end)