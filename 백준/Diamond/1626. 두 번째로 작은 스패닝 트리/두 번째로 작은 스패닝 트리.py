import sys
I,R = lambda:map(int,sys.stdin.readline().split()),range
sys.setrecursionlimit(60000)

log = 19
n,m = I()
r,L = R(n+1), R(18,-1,-1)
edges = [list(I()) for i in range(m)]
edges.sort(key=lambda x:x[2])
d = [[] for i in r]

parents = list(r)
def F(x):
    if x != parents[x]: parents[x] = F(parents[x])
    return parents[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b
def M(l):
    l = list(set(l))
    l.sort()
    return (l[-1],l[-2])
cost = 0
for a,b,c in edges:
    if F(a) != F(b):
        U(a,b)
        d[a].append((b,c))
        d[b].append((a,c))
        cost += c
if len(set([F(i) for i in r[1:]])) != 1:
    print(-1)
    exit(0)

p = [[0]*log for i in r]
mdist = [[(-1,-1) for j in R(log)] for i in r]
depth = [1]+[0]*n
def dfs(x,t):
    for nx,c in d[x]:
        if not depth[nx]:
            depth[nx] = t
            p[nx][0] = x
            mdist[nx][0] = (c,-1)
            dfs(nx,t+1)
dfs(1,2)

for k in R(1,log):
    for i in R(1,n+1):
        z=k-1
        x=p[i][z]
        mdist[i][k] = M([*mdist[i][z],*mdist[x][z],-1,-2])
        p[i][k] = p[x][z]

second = float('inf')

def fs(a,b):
    f,s = -1,-1
    if depth[a] < depth[b]:
        a,b = b,a
    for k in L:
        if depth[a] - depth[b] >= 1<<k:
            f,s = M([f,s,*mdist[a][k],-1])
            a = p[a][k]
    if a == b:
        return (f,s)

    for k in L:
        if p[a][k] != p[b][k]:
            f,s = M([f,s,*mdist[a][k],*mdist[b][k],-1])
            a,b= p[a][k],p[b][k]

    return M([f,s,mdist[a][0][0],mdist[b][0][0],-1])

for a,b,c in edges:
    f,s = fs(a,b)
    if f < 0:
        continue
    if f == c:
        if s >= 0:
            second = min(second, cost - s + c)
    else:
        second = min(second, cost - f + c)

print(-1 if second == float('inf') else second)

