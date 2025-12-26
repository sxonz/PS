from heapq import *

n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
heap = [(d[n-1][m-1],n-1,m-1)]
path = [[0]*m for i in range(n)]
path[n-1][m-1] = 1
visited = [[0]*m for i in range(n)]
visited[n-1][m-1] = 1

dx = (-1,1,0,0)
dy = (0,0,-1,1)

while heap:
    cur,x,y = heappop(heap)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if d[nx][ny] > cur:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    heappush(heap,(d[nx][ny],nx,ny))
                path[nx][ny] += path[x][y]
print(path[0][0])