import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
d = [[] for i in range(n+1)]
log = 21 
parents = [[0]*log for i in range(n+1)]
depth = [0]*(n+1)
visited = [False]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

def dfs(x):
    visited[x] = True
    for nx in d[x]:
        if not visited[nx]:
            depth[nx] = depth[x] + 1
            parents[nx][0] = x
            dfs(nx)

dfs(1)
for i in range(1,log):
    for j in range(1,n+1):
        parents[j][i] = parents[parents[j][i-1]][i-1]

def lca(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    for i in range(log-1,-1,-1):
        if depth[b] - depth[a] >= 1<<i:
            b = parents[b][i]
    if a == b:
        return a
    for i in range(log-1,-1,-1):
        if parents[a][i] != parents[b][i]:
            a,b = parents[a][i],parents[b][i]
    return parents[a][0]

m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))
