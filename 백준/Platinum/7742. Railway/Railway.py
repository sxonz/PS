import sys
sys.setrecursionlimit(100001)
log = 18
I = lambda:map(int,sys.stdin.readline().split())
n,q = I()
R = range(n+1)
d = [[] for i in R]
for i in range(n-1):
    a,b,c = I()
    d[a].append((b,c))
    d[b].append((a,c))

parents = [[0]*log for i in R]
distance = [0]*(n+1)
depth = [1]+[0]*n
def dfs(x):
    for nx,c in d[x]:
        if not depth[nx]:
            depth[nx] = depth[x] + 1
            distance[nx] = distance[x] + c
            parents[nx][0] = x
            dfs(nx)
dfs(1)

for k in range(1,log):
    for i in range(1,n+1):
        parents[i][k] = parents[parents[i][k-1]][k-1]

def lca(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    
    for k in range(log-1,-1,-1):
        if depth[b] - depth[a] >= 1<<k:
            b = parents[b][k]
    if a == b:
        return a
    for k in range(log-1,-1,-1):
        if parents[a][k] != parents[b][k]:
            a = parents[a][k]
            b = parents[b][k]
    return parents[a][0]

i = 0
while i != q:
    i += 1
    a,b = I()
    print(distance[a] + distance[b] - 2 * distance[lca(a,b)])