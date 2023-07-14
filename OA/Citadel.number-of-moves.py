from collections import *

# TC: O(n^2)  SC: O(n^2)
def number_of_moves(n, startx, starty, endx, endy):
    dq = deque([(startx, starty)])
    v = [[False]*n for _ in range(n)]
    ans = 0
    while dq:
        lenn = len(dq)
        for _ in range(lenn):
            x, y = dq.popleft()
            if x == endx and y == endy: return ans
            for dx, dy in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                nx = x+dx
                ny = y+dy
                if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                    dq.append((nx, ny))
                    v[nx][ny] = True
        ans += 1
    return -1

print(number_of_moves(9,4,4,4,8))  # 2
print(number_of_moves(9,4,4,10,5))  # -1