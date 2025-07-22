import sys
from heapq import *

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
visited[1] = True
heap = [1]
cur = 0
while heap:
    x = heappop(heap)
    if x-cur >= 2:
        print("NO")
        break
    cur = x
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            heappush(heap,nx)
else:
    print("YES")