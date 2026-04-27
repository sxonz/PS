from heapq import *
n,e = map(int,input().split())
d = [[0]*(n+1)for i in range(n+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    d[a][b] = c
    d[b][a] = c
m,m2 = map(int,input().split())
def r(x,y):
    if x == y:
        return 0
    distance = [0]*(n+1)
    visited = [0]*(n+1)
    heap = [(0,x)]
    while heap:
        cost,cx = heappop(heap)
        if distance[cx]:
            continue
        distance[cx] = cost
        visited[cx] = 1
        if cx == y:
            return cost
        for nx in range(1,n+1):
            if d[cx][nx]:
                heappush(heap,(cost+d[cx][nx],nx))
    else:
        return -1
res = -1
tmp = 0
for x,y in zip((1,m,m2),(m,m2,n)):
    if (t:=r(x,y)) == -1:
        print(-1)
        break
    tmp += t
else:
    res = tmp
    tmp = 0
    for x,y in zip((1,m2,m),(m2,m,n)):
        tmp += r(x,y)
    print(min(res,tmp))