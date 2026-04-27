n = int(input())
d = [0]+[(i+1,int(input())) for i in range(n)]

def dfs(x):
    if visited[x]:
        return x == i
    visited[x] = True
    return dfs(d[x][1])
res = []
for i in range(1,n+1):
    visited = [False]*(n+1)
    if dfs(i):
        res.append(i)
print(len(res))
print(*res,sep="\n")

