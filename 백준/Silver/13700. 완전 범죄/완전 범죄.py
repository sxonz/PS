from collections import deque

n,s,d,f,b,k = map(int,input().split())
if k:
    p = list(map(int,input().split()))
else:
    p = []
police = [0]*(n+1)
for i in p:
    police[i] = 1
queue = deque([s])
visited = [0]*(n+1)
distance = [0]*(n+1)
visited[s] = 1
while queue:
    x = queue.popleft()
    if x+f<=n and not visited[x+f] and not police[x+f]:
        visited[x+f] = 1
        distance[x+f] = distance[x] + 1
        queue.append(x+f)
    if 0<x-b and not visited[x-b] and not police[x-b]:
        visited[x-b] = 1
        distance[x-b] = distance[x] + 1
        queue.append(x-b)

if not visited[d]:
    print("BUG FOUND")
else:
    print(distance[d])