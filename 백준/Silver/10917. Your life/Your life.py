import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)

distance = [0]*(n+1)
queue = deque([1])
while queue:
    x = queue.popleft()
    for nx in d[x]:
        if not distance[nx]:
            distance[nx] = distance[x]+1
            queue.append(nx)

print(distance[n] if distance[n] else -1)