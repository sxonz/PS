import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    d[b].append(a)
    indegree[a] += 1

res = 0
ans = []
for i in range(1,n+1):
    queue = deque([i])
    visited = [0]*(n+1)
    visited[i] = 1
    cnt = 1
    while queue:
        x = queue.popleft()
        for nx in d[x]:
            if not visited[nx]:
                visited[nx] = 1
                queue.append(nx)
                cnt += 1
    if cnt > res:
        res = cnt
        ans = [i]
    elif cnt >= res:
        ans.append(i)

print(*sorted(ans))
                
