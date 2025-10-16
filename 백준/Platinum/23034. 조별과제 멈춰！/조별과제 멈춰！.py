import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(m)]
d.sort(key = lambda x:x[2])

parent = list(range(n+1))
def F(x):
    if x != parent[x]:
        parent[x] = F(parent[x])
    return parent[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

cost = 0
graph = [[] for i in range(n+1)]
for a,b,c in d:
    if F(a) != F(b):
        U(a,b)
        cost += c
        graph[a].append((b,c))
        graph[b].append((a,c))

log = 15
sparse = [[0]*log for i in range(n+1)]
maxdist = [[0]*log for i in range(n+1)]
depth = [0]*(n+1)

def dfs(x,par,t):
    depth[x] = t
    for nx,c in graph[x]:
        if nx != par:
            sparse[nx][0] = x
            maxdist[nx][0] = c
            dfs(nx,x,t+1)
dfs(1,-1,1)

for k in range(1,log):
    for i in range(1,n+1):
        sparse[i][k] = sparse[sparse[i][k-1]][k-1]
        maxdist[i][k] = max(maxdist[i][k-1],maxdist[sparse[i][k-1]][k-1])

def dist(a,b):
    if depth[b] < depth[a]:
        a,b = b,a
    ans = 0
    for k in range(log-1,-1,-1):
        if depth[b] - depth[a] >= 1<<k:
            ans = max(ans,maxdist[b][k])
            b = sparse[b][k]
    if a == b:
        return ans
    for k in range(log-1,-1,-1):
        if sparse[a][k] != sparse[b][k]:
            ans = max(ans,maxdist[a][k],maxdist[b][k])
            a = sparse[a][k]
            b = sparse[b][k]
    return max(ans,maxdist[a][0],maxdist[b][0])

q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    print(cost-dist(x,y))