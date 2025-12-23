from heapq import *
import sys
input = sys.stdin.readline

n,m,s,e = map(int,input().split())

d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

visited = [False]*(n+1)
distance = [0]*(n+1)
parents = [[] for i in range(n+1)]

heap = [(0,s,-1)]
while heap:
    dist,x,f = heappop(heap)
    if visited[x]:
        if distance[x] == dist:
            parents[x].append(f)
        continue
    visited[x] = True
    distance[x] = dist
    parents[x].append(f)

    for nx,cost in d[x]:
        if not visited[nx]:
            heappush(heap,(dist+cost,nx,x))

ans = set()
visited = [0]*(n+1)
visited[e] = 1
stack = [e]
while stack:
    x = stack.pop()
    ans.add(x)
    if -1 in parents[x]:
        continue
    for nx in parents[x]:
        if not visited[nx]:
            visited[nx] = 1
            stack.append(nx)
print(len(ans))
print(*sorted(list(ans)))