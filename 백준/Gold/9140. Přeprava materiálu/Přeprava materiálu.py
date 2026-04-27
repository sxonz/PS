from heapq import *
ans = []
while True:
    n,m,s,e = map(int,input().split())
    if n+m+s+e == 0:
        break
    d = [[] for i in range(n+1)]
    for i in range(m):
        a,b,c = map(int,input().split())
        d[a].append((b,c))
        d[b].append((a,c))
    heap = [(0,s)]
    visited = [False]*(n+1)
    distance = [0]*(n+1)
    while heap:
        cost,x = heappop(heap)
        if x == e:
            print(cost)
            break
        if visited[x]:
            continue
        visited[x] = True
        distance[x] = cost
        for nx,c in d[x]:
            if not visited[nx]:
                heappush(heap,(cost+c,nx))
