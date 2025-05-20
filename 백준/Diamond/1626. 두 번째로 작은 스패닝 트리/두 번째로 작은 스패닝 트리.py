import sys
input = sys.stdin.readline
sys.setrecursionlimit(60000)

log = 19
n,m = map(int,input().split())
edges = []
d = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

parents = list(range(n+1))
def F(x):
    if x != parents[x]: parents[x] = F(parents[x])
    return parents[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

cost = 0
for c,a,b in edges:
    if F(a) != F(b):
        U(a,b)
        d[a].append((b,c))
        d[b].append((a,c))
        cost += c
if len(set([F(i) for i in range(1,n+1)])) != 1:
    print(-1)
else:
    p = [[0]*log for i in range(n+1)]
    mdist = [[(-1,-1) for j in range(log)] for i in range(n+1)]
    depth = [0]*(n+1)
    visited = [0]*(n+1)
    depth[1] = 1
    visited[1] = 1

    def dfs(x):
        for nx,c in d[x]:
            if not visited[nx]:
                visited[nx] = 1
                depth[nx] = depth[x] + 1
                p[nx][0] = x
                mdist[nx][0] = (c,-1)
                dfs(nx)
    dfs(1)

    for k in range(1,log):
        for i in range(1,n+1):
            tmp = mdist[i][k-1]
            tmp2 = mdist[p[i][k-1]][k-1]
            dists = list(set([tmp[0],tmp[1],tmp2[0],tmp2[1],-1,-2]))
            dists.sort()
            mdist[i][k] = (dists[-1],dists[-2])
            p[i][k] = p[p[i][k-1]][k-1]

    second = float('inf')

    def fs(a,b):
        f,s = -1,-1
        if depth[a] < depth[b]:
            a,b = b,a
        for k in range(log-1,-1,-1):
            if depth[a] - depth[b] >= 1<<k:
                tmp = mdist[a][k]
                r = list(set([f,s,tmp[0],tmp[1],-1]))
                r.sort()
                f,s = r[-1],r[-2]
                a = p[a][k]
        if a == b:
            return (f,s)

        for k in range(log-1,-1,-1):
            if p[a][k] != p[b][k]:
                tmp = mdist[a][k]
                tmp2 = mdist[b][k]
                r = list(set([f,s,tmp[0],tmp[1],tmp2[0],tmp2[1],-1]))
                r.sort()
                f,s = r[-1],r[-2]
                a = p[a][k]
                b = p[b][k]

        r = list(set([f,s,mdist[a][0][0],mdist[b][0][0],-1]))
        r.sort()
        return (r[-1],r[-2])

    for c,a,b in edges:
        dists = fs(a,b)
        if dists[0] < 0:
            continue
        if dists[0] == c:
            if dists[1] >= 0:
                second = min(second, cost - dists[1] + c)
        else:
            second = min(second, cost - dists[0] + c)

    if second == float('inf'):
        print(-1)
    else:
        print(second)

