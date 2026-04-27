from heapq import *

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
s,t = map(int,input().split())
heap = [(0,s)]
distance = [-1]*(n+1)
while heap:
    cost,x = heappop(heap)
    if distance[x] != -1:
        continue
    distance[x] = cost
    if x == t:
        print(cost)
        break
    for nx,c in d[x]:
        heappush(heap,(cost+c,nx))