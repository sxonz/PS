n,m,s,v = map(int,input().split())
d = [tuple(map(float,input().split())) for i in range(n)]
es = [tuple(map(float,input().split())) for i in range(m)]

graph = [[] for i in range(n)]
for i in range(n):
    for j in range(m):
        if ((d[i][0]-es[j][0])**2 + (d[i][1]-es[j][1])**2)**0.5 <= v*s:
            graph[i].append(j)

connected = [-1]*m
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True

    for nx in graph[x]:
        if connected[nx] == -1 or dfs(connected[nx]):
            connected[nx] = x
            return True
    return False

cnt = n
for i in range(n):
    visited = [0]*n
    cnt -= dfs(i)
print(cnt)