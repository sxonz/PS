import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

log = 18

n = int(input())
d = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

depth = [0]*(n+1)
parents = [[0]*log for _ in range(n+1)]
minimum = [[int(1e10)]*log for _ in range(n+1)]
maximum = [[-1]*log for _ in range(n+1)]

visited = [False]*(n+1)
visited[1] = True

def dfs(x):
    for nx,c in d[x]:
        if not visited[nx]:
            visited[nx] = True
            depth[nx] = depth[x] + 1
            parents[nx][0] = x
            minimum[nx][0] = c
            maximum[nx][0] = c
            dfs(nx)
dfs(1)

for k in range(1,log):
    for i in range(1,n+1):
        minimum[i][k] = min(minimum[i][k-1],minimum[parents[i][k-1]][k-1])
        maximum[i][k] = max(maximum[i][k-1],maximum[parents[i][k-1]][k-1])
        parents[i][k] = parents[parents[i][k-1]][k-1]

def lca(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    minres = int(1e10)
    maxres = -1
    for k in range(log-1,-1,-1):
        if depth[a] <= depth[parents[b][k]]:
            minres = min(minres,minimum[b][k])
            maxres = max(maxres,maximum[b][k])
            b = parents[b][k]

    if a == b:
        return (minres,maxres)
    
    for k in range(log-1,-1,-1):
        if parents[a][k] != parents[b][k]:
            minres = min(minres,minimum[a][k],minimum[b][k])
            maxres = max(maxres,maximum[a][k],maximum[b][k])
            a = parents[a][k]
            b = parents[b][k]
    
    return (min(minres,minimum[a][0],minimum[b][0]),max(maxres,maximum[a][0],maximum[b][0]))

m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(*lca(a,b))