from heapq import *

n,m = map(int,input().split())
d = [[] for _ in range(101)]
ladder = {}
for _ in range(n+m):
    x,y = map(int,input().split())
    d[x].append(y)
    ladder[x] = y
for i in range(1,100):
    for j in range(1,7):
        if i+j < 101:
            d[i].append(i+j)

queue = [(0,1)]
visited = [False]*101
distance = [0]*101
while queue:
    s,x = heappop(queue)
    if x in ladder:
        heappush(queue,(s,ladder[x]))
        continue
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            distance[nx] = s + 1
            heappush(queue,(distance[nx],nx))
print(distance[100])