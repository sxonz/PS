from heapq import *

n,m,x = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))

come = [0]*(n+1)

def dijkstra(s,e):
    heap = [(0,s)]
    visited = [False]*(n+1)
    visited[s] = True
    while heap:
        c,cur = heappop(heap)
        visited[cur] = True
        if cur == e:
            return c
        for nx,cost in d[cur]:
            if not visited[nx]:
                heappush(heap,(c+cost,nx))
        
print(max([dijkstra(i,x)+dijkstra(x,i) for i in range(1,n+1)]))


