import time

from collections import deque

n = int(input())
start = time.time()
d = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
Time = [0]*(n+1)

for cur in range(1,n+1):

    tmp = deque(list(map(int,input().split())))
    t = tmp.popleft()
    Time[cur] = t

    f = tmp.popleft()
    for i in range(f):
        d[tmp[i]].append(cur)
        indegree[cur] += 1

queue = deque([])

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

p = [0]*(n+1)
while queue:
    x = queue.popleft()

    for nx in d[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            queue.append(nx)
        p[nx] = max(p[nx],p[x] + Time[x])

m = 0
for i in range(1,n+1):
    m = max(m,Time[i]+p[i])

print(m)