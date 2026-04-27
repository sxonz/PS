from heapq import *
n,m = map(int,input().split())

d = [[] for i in range(n)]
r = list(map(int,input().split()))
for i in range(m):
    a,b,c = map(int,input().split())
    if (r[a] and a!=n-1) or (r[b] and b!=n-1):
        continue
    d[a].append((b,c))
    d[b].append((a,c))

heap = [(0,0)]
distance = [0]*n
while heap:
    cost,x = heappop(heap)
    if distance[x]:
        continue
    distance[x] = cost
    if x == n-1:
        print(cost)
        break
    for nx,c in d[x]:
        heappush(heap,(cost+c,nx))
else:
    print(-1)