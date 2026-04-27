from heapq import *
n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
heap = [(0,1)]
INF = int(1e10)
distance = [INF]*(n+1)
distance[1] = 0
visited = [False]*(n+1)
visited[1] = True
while heap:
    dis,x = heappop(heap)
    visited[x] = True
    distance[x] = dis
    if x == n:
        break
    for nx,cost in d[x]:
        if not visited[nx]:
            heappush(heap,(dis+cost,nx))
print(dis)