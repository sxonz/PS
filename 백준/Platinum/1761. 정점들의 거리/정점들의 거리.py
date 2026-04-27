import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

log = 17

n = int(input())
d = [[] for _ in range(n+1)]
parents = [[1]*log for _ in range(n+1)]
distance = [[0]*log for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

depth = [0]*(n+1)
visited = [False]*(n+1)
visited[1] = True
def dfs(x):
    for nx,c in d[x]:
        if not visited[nx]:
            visited[nx] = True
            depth[nx] = depth[x] + 1
            parents[nx][0] = x
            distance[nx][0] = c
            dfs(nx)
dfs(1)

for k in range(1,log):
    for i in range(1,n+1):
        parents[i][k] = parents[parents[i][k-1]][k-1]
        distance[i][k] = distance[i][k-1] + distance[parents[i][k-1]][k-1]

def lca(a,b):
    cost = 0

    if depth[a] > depth[b]:
        a,b = b,a
    
    for k in range(log-1,-1,-1):
        if depth[a] <= depth[parents[b][k]]:
            cost += distance[b][k]
            b = parents[b][k]

    if a == b:
        return cost
    
    for k in range(log-1,-1,-1):
        if parents[a][k] != parents[b][k]:
            cost += distance[a][k] + distance[b][k]
            a = parents[a][k]
            b = parents[b][k]
    return cost + distance[a][0] + distance[b][0]

m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))