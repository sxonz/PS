from collections import deque

n = int(input())
k = int(input())
d = [[] for _ in range(n+1)]
d2 = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for i in range(k):
    a,b,c = map(int,input().split())
    indegree[b] += 1
    d[a].append((b,c))
    d2[b].append((a,c))

queue = deque([])
start,end = map(int,input().split())

queue.append(start)

distance = [0]*(n+1)
while queue:
    x = queue.popleft()
    for nx,cost in d[x]:
        indegree[nx] -= 1
        distance[nx] = max(distance[nx],distance[x]+cost)
        if indegree[nx] == 0:
            queue.append(nx)

queue.append(end)
cnt = 0
visited = [False]*(n+1)

while queue:
    x = queue.popleft()
    visited[x] = True
    for nx,cost in d2[x]:
        if distance[nx]+cost == distance[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
            cnt += 1

print(distance[end])
print(cnt)