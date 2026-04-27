from collections import deque

import sys
sys.setrecursionlimit(200000)

def dfs(x):
    for nx,p in d[x]:
        if visited[nx] == -1:
            visited[nx] = visited[x] + p
            dfs(nx)

n = int(input())
d = [[] for _ in range(n+1)]

for _ in range(n):
    a,*temp = map(int,input().split())
    temp = deque(temp)
    while temp[0] != -1:
        b,c = temp.popleft(),temp.popleft()
        d[a].append((b,c))
        d[b].append((a,c))

visited = [-1]*(n+1)
visited[1] = 0
dfs(1)

temp = visited.index(max(visited))
visited = [-1]*(n+1)
visited[temp] = 0
dfs(temp)

print(max(visited))
