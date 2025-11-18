import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visited = [False]*(n+1)
visited[1] = True
distance = [0]*(n+1)
queue = deque([1])
while queue:
    x = queue.popleft()
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            distance[nx] = distance[x] + 1
            queue.append(nx)

rev = {}
visited = [False]*(n+1)
visited[n] = True
queue = deque([n])
while queue:
    x = queue.popleft()
    if distance[x] not in rev:
        rev[distance[x]] = []
    rev[distance[x]].append(x)
    for nx in d[x]:
        if not visited[nx] and distance[nx] == distance[x]-1:
            queue.append(nx)
            visited[nx] = True
for i in range(distance[n]-1,-1,-1):
    if len(rev[i]) == 1:
        print(rev[i][0])
        break