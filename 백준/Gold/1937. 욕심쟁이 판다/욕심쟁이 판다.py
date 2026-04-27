import sys
sys.setrecursionlimit(30000)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
dp = {} 

def dfs(x, y):
    if (x, y) in dp:
        return dp[(x, y)]
    
    long = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and d[nx][ny] < d[x][y]:
            long = max(long, 1 + dfs(nx, ny))
    
    dp[(x, y)] = long
    return long

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
