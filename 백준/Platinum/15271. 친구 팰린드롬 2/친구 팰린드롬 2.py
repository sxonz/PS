n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    if a%2==b%2:
        continue
    if a%2 == 0:
        a,b = b,a
    d[a].append(b)

connected = [0]*(n+1)

def dfs(x):
    if visited[x]:
        return False
    visited[x] = True
    for nx in d[x]:
        if not connected[nx] or dfs(connected[nx]):
            connected[nx] = x
            return True
        
    return False

cnt = 0
for i in range(1,n+1):
    visited = [False]*(n+1)
    cnt += dfs(i)
print(cnt*2+(cnt*2<n))