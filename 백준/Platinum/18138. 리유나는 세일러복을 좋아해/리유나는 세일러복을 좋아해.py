n,m = map(int,input().split())
a = [int(input()) for i in range(n)]
b = [int(input()) for j in range(m)]

d = [[] for i in range(n)]

for i in range(n):
    for j in range(m):
        if a[i]/2 <= b[j] <= a[i]*3/4 or a[i] <= b[j] <= a[i]*5/4:
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
    visited = [0]*n
    cnt += dfs(i)

print(cnt)