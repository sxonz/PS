from heapq import *

dx = (-1,1,0,0)
dy = (0,0,-1,1)

m,n = map(int,input().split())
d = [list(input()) for i in range(n)]
tmp = []
for i in range(n):
    for j in range(m):
        if d[i][j] == "C":
            tmp.append((i,j))
s,e = tmp

visited = [[[False]*4 for j in range(m)] for i in range(n)]
heap = [(0,s[0],s[1],0),(0,s[0],s[1],1),(0,s[0],s[1],2),(0,s[0],s[1],3)]
while heap:
    cost,x,y,dir = heappop(heap)
    if visited[x][y][dir]:
        continue

    visited[x][y][dir] = True
    if (x,y) == e:
        print(cost)
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny][i] and d[nx][ny] != "*":
                if dir == i:
                    heappush(heap,(cost,nx,ny,i))
                else:
                    heappush(heap,(cost+1,nx,ny,i))
