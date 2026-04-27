from collections import deque

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
indegree[0] = -1

for _ in range(m):
    a,b = map(int,input().split())
    indegree[b] += 1
    d[a].append(b)

queue = deque([])
res = [0]*(n+1)

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

time = 1
while queue:
    tmp = []
    while queue:
        tmp.append(queue.popleft())

    for x in tmp:
        res[x] = time
        for nx in d[x]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                queue.append(nx)
    time += 1
print(*res[1:])