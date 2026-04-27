import sys
sys.setrecursionlimit(30001)
log = 16
n = int(input())
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
parents = [[1]*log for i in range(n+1)]
depth = [0]*(n+1)
depth[1] = 1
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
    res = 0
    if depth[a] > depth[b]:
        a,b = b,a
    for k in range(log-1,-1,-1):
        if depth[b]-depth[a] >= 1<<k:
            b = parents[b][k]
            res += 1<<k

    if a == b:
        return res
    
    for k in range(log-1,-1,-1):
        if parents[a][k] != parents[b][k]:
            a = parents[a][k]
            b = parents[b][k]
            res += 2<<k
    
    return res + 2



m = int(input())
a = int(input())
res = 0
for i in range(m-1):
    b = int(input())
    res += lca(a,b)
    a = b

print(res)


