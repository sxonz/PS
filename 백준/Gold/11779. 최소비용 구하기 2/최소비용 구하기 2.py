import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
m = int(input())

d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a].append((b,c))

s,e = map(int,input().split())
heap = [(0,s,0)]

visited = [False]*(n+1)
parents = [-1]*(n+1)
while heap:
    cur,x,p = heappop(heap)
    if visited[x]:
        continue
    parents[x] = p
    if x == e:
        break
    visited[x] = True
    for nx,cost in d[x]:
        if not visited[nx]:
            heappush(heap,(cur+cost,nx,x))

ans = []
while e:
    ans.append(e)
    e = parents[e]

print(cur)
print(len(ans))
print(*ans[::-1])
            