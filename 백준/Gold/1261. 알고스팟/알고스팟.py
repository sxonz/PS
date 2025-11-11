from heapq import *
dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(map(int,input())) for i in range(m)]

heap = [(0,0,0)]
visited = [[False]*n for i in range(m)]

while heap:
    dist,x,y = heappop(heap)
    if visited[x][y]:
        continue
    visited[x][y] = True

    if (x,y) == (m-1,n-1):
        print(dist)
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
            heappush(heap,(dist+d[nx][ny],nx,ny))
