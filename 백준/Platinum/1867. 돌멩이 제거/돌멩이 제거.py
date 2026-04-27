n,k = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(k):
    a,b = map(int,input().split())
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
ans = 0
for i in range(1,n+1):
    visited = [False] * (n+1)
    ans += dfs(i)
print(ans)