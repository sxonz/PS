n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(1,n+1):
    v,*r = map(int,input().split())
    for j in r:
        d[i].append(j)

connect = [0]*(m+1)
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True
    
    for nx in d[x]:
        if not connect[nx] or dfs(connect[nx]):
            connect[nx] = x
            return True
    
    return False

for i in range(1,n+1):
    visited = [False]*(n+1)
    dfs(i)

print(sum([bool(i) for i in connect]))