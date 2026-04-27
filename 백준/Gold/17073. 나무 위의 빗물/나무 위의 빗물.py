from collections import deque
import sys
I = lambda:map(int,sys.stdin.readline().split())

n,k = I()
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = I()
    d[a].append(b)
    d[b].append(a)

visited = [False]*(n+1)
visited[1] = True

queue = deque([1])
cnt = 0
while queue:
    x = queue.popleft()
    flag = True
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            flag = False
            queue.append(nx)
    if flag:
        cnt += 1
print(k/cnt)