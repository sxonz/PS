from itertools import combinations
from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
com = []
virus = []
w = 0
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            com.append((i,j))
        elif d[i][j] == 2:
            virus.append((i,j))
        else:
            w += 1
walls = set(combinations(com,3))
def bfs(wall):
    a,b,c = wall
    cnt = n*m - w

    d[a[0]][a[1]] = 1
    d[b[0]][b[1]] = 1
    d[c[0]][c[1]] = 1
    queue = deque(virus)
    visited = [[False]*m for _ in range(n)]

    while queue:
        x,y = queue.popleft()
        cnt -= 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and d[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    d[a[0]][a[1]] = 0
    d[b[0]][b[1]] = 0
    d[c[0]][c[1]] = 0
    return cnt


res = []
for i in walls:
    res.append(bfs(i))
print(max(res)-3)