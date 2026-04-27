from collections import deque

n,m,k = map(int,input().split())
costs = list(map(int,input().split()))
costs.insert(0,0)

d = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
queue = deque([])
visited = [False]*(n+1)
res = 0
for i in range(1,n+1):
    c = 314159265358979
    flag = False
    if not visited[i]:
        queue.append(i)
        visited[i] = True
        flag = True
        while queue:
            x = queue.popleft()
            c = min(c,costs[x])
            for nx in d[x]:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
    if flag:
        res += c

if res > k:
    print('Oh no')
else:
    print(res)