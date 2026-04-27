def dfs(x,cnt):
    for nx in d[x]:
        if not visit[nx]:
            visit[nx] = True
            cnt = dfs(nx,cnt+1)
    return cnt
    

n = int(input())
d = [[] for _ in range(n+1)]

for i in range(int(input())):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visit = [False]*(n+1)
visit[1] = True
print(dfs(1,0))