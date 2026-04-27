n,m = map(int,input().split())
r = 1
parents = [-1,-1]
d = [[] for i in range(n+1)]
for i in range(2,n+1):
    parents.append(p := int(input()))
    d[p].append(i)

depth = [0]*(n+1)
def dfs(x):
    for nx in d[x]:
        depth[nx] = depth[x] + 1
        dfs(nx)
dfs(1)
for i in range(m):
    a,b = map(int,input().split())
    if depth[a] > depth[b]:a,b = b,a
    while depth[b] > depth[a]:
        b = parents[b]
    while a!=b:
        a,b = parents[a],parents[b]
    print(a)