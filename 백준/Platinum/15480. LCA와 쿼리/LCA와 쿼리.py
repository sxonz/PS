import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

log = 18
n = int(input())
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

depth = [0]*(n+1)
depth[1] = 1
parents = [[0]*log for i in range(n+1)]

def dfs(x):
    for nx in d[x]:
        if not depth[nx]:
            depth[nx] = depth[x] + 1
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
        if parents[b][k] != parents[a][k]:
            a = parents[a][k]
            b = parents[b][k]
    return parents[a][0]

for i in range(int(input())):
    r,a,b = map(int,input().split())
    print(min([lca(a,b),lca(r,a),lca(r,b)],key=lambda x:-depth[x]))
    