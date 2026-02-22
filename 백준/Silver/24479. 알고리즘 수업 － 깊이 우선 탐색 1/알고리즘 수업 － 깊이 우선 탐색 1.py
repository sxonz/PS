import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
n,m,r = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
for i in d:
    i.sort()

visited = [0]*(n+1)
ans = [0]*(n+1)
cur = 1
def dfs(x):
    global cur
    ans[x] = cur
    cur += 1
    visited[x] = 1
    for nx in d[x]:
        if not visited[nx]:
            dfs(nx)

dfs(r)
print(*ans[1:],sep='\n')