from collections import deque

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

queue = deque([])
queue.append(1)
visited = [False]*(n+1)
visited[1] = True
distance = [0]*(n+1)

while queue:
    x = queue.popleft()
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            distance[nx] = distance[x] + 1
            queue.append(nx)
print(distance.index(max(distance)),max(distance),distance.count(max(distance)))