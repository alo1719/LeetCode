from collections import deque


# TC: O(mn), SC: O(mn)
def drive(m, n, obstacles, goal, move, change, start):
    start_pos = (0, start)
    dq = deque()
    cost = [[-1]*n for _ in range(m)]
    cost[0][start] = 0
    dq.append(start_pos)
    while dq:
        x, y = dq.popleft()
        if x == m-1 and y == goal:
            return cost[x][y]
        if x+1 < m and (x+1, y) not in obstacles and cost[x+1][y] == -1:
            cost[x+1][y] = cost[x][y]+move
            dq.append((x+1, y))
        if y-1 >= 0 and (x, y-1) not in obstacles and cost[x][y-1] == -1:
            cost[x][y-1] = cost[x][y]+change
            dq.append((x, y-1))
        if y+1 < n and (x, y+1) not in obstacles and cost[x][y+1] == -1:
            cost[x][y+1] = cost[x][y]+change
            dq.append((x, y+1))

print(drive(5, 5, [(1,1),(3,1),(2,3),(4,4)], 3, 1, 2, 2))  # 6
print(drive(5, 5, [(1,1),(3,1),(2,3),(4,4)], 3, 2, 1, 2))  # 9
print(drive(5, 5, [(1,1),(3,1),(3,0),(3,2),(2,3),(4,4)], 1, 1, 2, 2))  # 14
