from collections import deque

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
q = []
for i in range(m):
    a,b = map(int,input().split())
    q.append((a,b))

res = ['wow']
for i in range(1,n+1):
    queue = deque([])
    visited = [False]*(n+1)
    visited[i] = True
    distance = [0]*(n+1)
    queue.append(i)
    while queue:
        x = queue.popleft()
        for nx,cost in d[x]:
            if not visited[nx]:
                visited[nx] = True
                distance[nx] = distance[x] + cost
                queue.append(nx)
    res.append(distance)

for a,b in q:
    print(res[a][b])