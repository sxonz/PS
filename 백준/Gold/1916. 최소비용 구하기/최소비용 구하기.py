import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

d = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))

v,k = map(int,input().split())

dist = [INF]*(n+1)
dist[v] = 0

heap = [(0,v)]

while heap:
    cost,node = heappop(heap)

    if dist[node] < cost:
        continue

    for i,c in d[node]:
        if cost+c < dist[i]:
            dist[i] = cost+c
            heappush(heap,[dist[i],i])
print(dist[k])