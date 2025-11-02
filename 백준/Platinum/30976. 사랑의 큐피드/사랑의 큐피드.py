n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a2 = list(map(int,input().split()))
b2 = list(map(int,input().split()))

d = [[] for i in range(n)]
for i in range(n):
    for j in range(m):
        if a[i] > b2[j] and b[j] < a2[i]:
            d[i].append(j)

connected = [-1]*m

def dfs(x):
    if visited[x]:
        return False
    visited[x] = True

    for nx in d[x]:
        if connected[nx] == -1 or dfs(connected[nx]):
            connected[nx] = x
            return True
    
    return False

cnt = 0
for i in range(n):
    visited = [False]*n
    cnt += dfs(i)

print(cnt)