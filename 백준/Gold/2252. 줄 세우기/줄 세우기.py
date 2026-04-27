from collections import deque

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]

indegree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    indegree[b] += 1

queue = deque([])
for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

ans = []
while queue:
    x = queue.popleft()
    ans.append(x)
    for nx in d[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            queue.append(nx)

print(*ans)