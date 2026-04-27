from heapq import *

dx = (-1,0,1,0)
dy = (0,-1,0,1)

n,m,t = map(int,input().split())
d = [input() for i in range(n)]

visited = [[[0,0,0,0] for i in range(m)] for j in range(n)]
heap = []
for i in range(n):
    for j in range(m):
        if d[i][j] in "0123":
            heap.append((0,i,j,int(d[i][j])))

while heap:
    time,x,y,dir = heappop(heap)
    if not (0<=x<n and 0<=y<m) or visited[x][y][dir]:
        continue

    visited[x][y][dir] = 1
    if d[x][y] == "S":
        print(time)
        break

    if d[x][y] == "T":
        heappush(heap,(time,x+dx[(dir+1)%4],y+dy[(dir+1)%4],(dir+1)%4))
    else:
        if not visited[x][y][(dir+1)%4]:
            heappush(heap,(time+t,x,y,(dir+1)%4))

        if 0<=x+dx[(dir+1)%4]<n and 0<=y+dy[(dir+1)%4]<m and not visited[x+dx[(dir+1)%4]][y+dy[(dir+1)%4]][dir]:
            heappush(heap,(time+1,x+dx[(dir+1)%4],y+dy[(dir+1)%4],dir))
        if 0<=x+dx[(dir+3)%4]<n and 0<=y+dy[(dir+3)%4]<m and not visited[x+dx[(dir+3)%4]][y+dy[(dir+3)%4]][dir]:
            heappush(heap,(time+1,x+dx[(dir+3)%4],y+dy[(dir+3)%4],dir))
else:
    print(-1)