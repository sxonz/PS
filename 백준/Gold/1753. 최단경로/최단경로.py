import heapq

INF = int(1e9)
n,m = map(int,input().split())
v = int(input())
d = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))

dist = [INF]*(n+1)
dist[v] = 0

heap = [[0,v]]
while heap:
    cost,node = heapq.heappop(heap)
    if dist[node] < cost:
        continue

    for i,c in d[node]:
        if dist[i] > cost+c:
            dist[i] = cost+c
            heapq.heappush(heap, [dist[i],i])
            
for i in range(1,n+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])