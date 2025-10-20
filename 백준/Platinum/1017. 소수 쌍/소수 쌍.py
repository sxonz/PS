def prime(x):
    for i in range(2,int(x**0.5+1)):
        if x%i == 0:
            return False
    return True
n = int(input())
d = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
for i in range(n):
    for j in range(i+1,n):
        if prime(d[i]+d[j]):
            if d[i]%2==d[0]%2:
                graph[i].append(j)
            else:
                graph[j].append(i)



def dfs(x):
    if visited[x]:
        return False
    visited[x] = True

    for nx in graph[x]:
        if connected[nx] == -1 or dfs(connected[nx]):
            connected[nx] = x
            return True
    return False

ans = []
for cur in graph[0]:
    connected = [-1]*n
    connected[cur] = 0
    for i in range(1,n):
        visited = [False]*n
        visited[0] = True
        if d[i]%2 == d[0]%2:
            dfs(i)
    if sum([1 for i in connected if i+1]) == n//2:
        ans.append(d[cur])
if ans:
    print(*sorted(ans))
else:
    print(-1)