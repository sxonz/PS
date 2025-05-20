import sys
input = sys.stdin.readline

log = 19
n,m = map(int,input().split())
edges = []
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
sedges = sorted(edges)

p = list(range(n+1))
def F(x):
    if x != p[x]: p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
cost = 0
d = [[] for i in range(n+1)]
for c,a,b in sedges:
    if F(a) != F(b):
        U(a,b)
        cost += c
        d[a].append((b,c))
        d[b].append((a,c))
root = 1
parents = [[0]*log for i in range(n+1)]
maximum = [[0]*log for i in range(n+1)]
depth = [0]*(n+1)
depth[1] = 1
visited = [0]*(n+1)
visited[1] = 1
def dfs(x):
    for nx,c in d[x]:
        if not visited[nx]:
            visited[nx] = 1
            depth[nx] = depth[x] + 1
            parents[nx][0] = x
            maximum[nx][0] = c
            dfs(nx)
dfs(1)
for k in range(1,log):
    for i in range(1,n+1):
        parents[i][k] = parents[parents[i][k-1]][k-1]
        maximum[i][k] = max(maximum[i][k-1],maximum[parents[i][k-1]][k-1])

def maxdist(a,b):
    maxcost = 0
    if depth[a] > depth[b]:
        a,b = b,a
    for k in range(log-1,-1,-1):
        if depth[b] - depth[a] >= 1<<k:
            maxcost = max(maxcost,maximum[b][k])
            b = parents[b][k]
    if a == b:
        return maxcost
    
    for k in range(log-1,-1,-1):
        if parents[a][k] != parents[b][k]:
            maxcost = max(maxcost,maximum[a][k],maximum[b][k])
            a = parents[a][k]
            b = parents[b][k]
    return max(maxcost,maximum[a][0],maximum[b][0])

for c,a,b in edges:
    print(cost-maxdist(a,b)+c)