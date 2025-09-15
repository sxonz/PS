n = int(input())
d = [[] for i in range(n)]
for i in range(n):
    s = list(map(int,input().split()))
    for j in range(n):
        if s[j]:
            d[i].append(j)
r = [[0]*n for i in range(n)]
def dfs(start,x):
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            r[start][nx] = 1
            dfs(start,nx)
    
for i in range(n):
    visited = [0]*n
    dfs(i,i)

for i in r:
    print(*i)