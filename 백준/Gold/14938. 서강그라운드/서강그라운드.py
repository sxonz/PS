from heapq import *

n,m,k = map(int,input().split())
d = [0]+list(map(int,input().split()))
graph = [[] for i in range(n+1)]

for i in range(k):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

ans = 0
for i in range(1,n+1):
    visited = [False]*(n+1)
    heap = [(0,i)]
    cur = 0
    while heap:
        dist,x = heappop(heap)
        if visited[x]:
            continue
        visited[x] = True
        cur += d[x]

        for nx,cost in graph[x]:
            if not visited[nx] and dist+cost <= m:
                heappush(heap,(dist+cost,nx))
    ans = max(ans,cur)


print(ans)
