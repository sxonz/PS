from heapq import *
dx = (-1,1,0,0)
dy = (0,0,-1,1)

for t in range(int(input())):
    n,m = map(int,input().split())
    d = [list(map(int,input().split())) for i in range(n)]
    visited = [[0]*m for i in range(n)]
    distance = [[0]*m for i in range(n)]
    heap = []
    for i in range(n):
        heappush(heap,(d[i][0],i,0))
        heappush(heap,(d[i][m-1],i,m-1))
    for i in range(m):
        heappush(heap,(d[0][i],0,i))
        heappush(heap,(d[n-1][i],n-1,i))
    
    while heap:
        dist,x,y = heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = 1
        distance[x][y] = dist
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    heappush(heap,(dist+d[nx][ny],nx,ny))
    maxv = 0
    for i in range(n):
        for j in range(m):
            if not d[i][j]:
                maxv = max(maxv,distance[i][j])
    ans = 0
    for i in range(n):
        for j in range(m):
            if not d[i][j] and distance[i][j] == maxv:
                ans +=1
    print(maxv,ans)