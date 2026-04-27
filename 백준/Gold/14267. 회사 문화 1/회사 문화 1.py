from collections import deque

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
p = list(map(int,input().split()))
r = 0
for i in range(n):
    if p[i] == -1:
        r = i+1
        continue
    d[p[i]].append(i+1)
comp = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    comp[a] += b

visited = [False]*(n+1)
queue = deque([r])
while queue:
    x = queue.popleft()
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            queue.append(nx)
            comp[nx] += comp[x]
print(*comp[1:])