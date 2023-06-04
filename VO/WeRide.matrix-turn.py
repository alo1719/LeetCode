from collections import deque


# TC: O(mn), SC: O(mn)
def matrix_turn(matrix):
    m, n = len(matrix), len(matrix[0])
    dq = deque()
    dq.append((0, 0))
    dp = [[-1] * n for _ in range(m)]
    dp[0][0] = 0
    while dq:
        x, y = dq.popleft()
        if x == m-1 and y == n-1:
            return dp[x][y]
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx = x + dx
            ny = y + dy
            # while makes it walk till the end
            while 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 0 and dp[nx][ny] == -1:
                dp[nx][ny] = dp[x][y] + 1
                dq.append((nx, ny))
                nx += dx
                ny += dy
    return -1

print(matrix_turn([[0,0,1],[0,1,0],[0,0,0]])) # 2
print(matrix_turn([[0,0,0],[0,0,0],[0,0,0]])) # 2