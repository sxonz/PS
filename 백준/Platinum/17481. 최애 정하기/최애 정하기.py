n,m = map(int,input().split())
d = dict()
for i in range(m):
    d[input()] = i

graph = [[] for i in range(n)]
for i in range(n):
    r,*w = input().split()
    graph[i] = [d[j] for j in w]

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

cnt = 0
for i in range(n):
    visited = [0]*n
    cnt += dfs(i)
if cnt == n:
    print("YES")
else:
    print("NO")
    print(cnt)