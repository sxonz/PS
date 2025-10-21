n,m,k = map(int,input().split())
d = [[]]
for i in range(n):
    d.append(list(map(int,input().split()[1:])))

connected = [0]*(m+1)
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
    visited = [False]*(n+1)
    ans += dfs(i)

cur = 0
for i in range(1,n+1):
    while cur < k:
        visited = [False]*(n+1)
        if dfs(i):
            cur += 1
        else:
            break
print(ans + cur)

    