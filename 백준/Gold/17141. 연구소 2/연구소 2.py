from itertools import combinations
from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
pos = []
cnt = n*n
for i in range(n):
    for j in range(n):
        if d[i][j] == 2:
            pos.append((i,j))
        elif d[i][j] == 1:
            cnt -= 1
            

ans = int(1e9)
for p in combinations(pos,m):
    distance = [[-1]*n for i in range(n)]
    cur = cnt

    queue = deque([])
    for i in p:
        queue.append(i)
        distance[i[0]][i[1]] = 0
    
    while queue:
        x,y = queue.popleft()
        cur -= 1
        if not cur:
            ans = min(ans,distance[x][y])
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and distance[nx][ny] == -1 and d[nx][ny] != 1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
if ans == int(1e9):
    ans = -1
print(ans)

