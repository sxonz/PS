from heapq import *
n,m,s,e = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
heap = [(0,s)]
distance = [0]*(n+1)
while heap:
    cost,x = heappop(heap)
    if distance[x]:
        continue
    distance[x] = cost
    if x == e:
        break
    for nx,c in d[x]:
        heappush(heap,(cost+c,nx))
print(distance[e])