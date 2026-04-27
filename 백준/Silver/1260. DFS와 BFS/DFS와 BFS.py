from collections import deque
import sys

sys.setrecursionlimit(2000)

def dfs(x):
    d.append(x)
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx)


def bfs():
    while queue:
        x = queue.popleft()
        b.append(x)
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)



n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
    
visited = [False]*(n+1)
visited[v] = True
d = []
b = []
dfs(v)

visited = [False]*(n+1)
visited[v] = True

queue = deque([v])
bfs()

print(' '.join(list(map(str,d))))
print(' '.join(list(map(str,b))))
