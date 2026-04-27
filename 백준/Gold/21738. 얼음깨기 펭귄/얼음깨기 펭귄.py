import sys
from collections import deque

I = lambda:map(int,sys.stdin.readline().split())
n,s,p = I()
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = I()
    d[a].append(b)
    d[b].append(a)

visited = [False]*(n+1)
distance = [0]*(n+1)

queue = deque([p])
while queue:
    x = queue.popleft()
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            distance[nx] = distance[x] + 1
            queue.append(nx)
print(n - sum(sorted([distance[i] for i in range(1,s+1)])[:2]) - 1)