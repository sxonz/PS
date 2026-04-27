n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]

graph = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][0] >= d[j][0] and d[i][1] >= d[j][1] and d[i][2] >= d[j][2] and i-j:
            if d[i] == d[j]:
                graph[min(i,j)].append(max(i,j))
            else:
                graph[i].append(j)

connected = [-1]*n
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True

    for nx in graph[x]:
        if connected[nx] == -1 or dfs(connected[nx]):
            connected[nx] = x
            return True
    return False

ans = n
for k in range(2):
    for i in range(n):
        visited = [0]*n
        ans -= dfs(i)
print(ans)