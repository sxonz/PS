import sys
input = sys.stdin.readline
from heapq import *

for _ in range(int(input())):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    d = [[] for i in range(n+1)]
    for i in range(m):
        a,b,c = map(int,input().split())
        d[a].append((b,c))
        d[b].append((a,c))
    e = [int(input()) for i in range(t)]
    heap = [(0,s,1)]
    visited = [0]*(n+1)
    use = [1]*(n+1)
    while heap:
        dist,x,f = heappop(heap)
        if visited[x]:
            continue
        visited[x] = 1
        use[x] = f
        for nx,c in d[x]:
            if not visited[nx]:
                nf = f
                if (x,nx)==(g,h) or (nx,x) == (g,h):
                    nf = 0
                heappush(heap,(dist+c,nx,nf))
    print(*[i for i in sorted(e) if use[i]^1])
