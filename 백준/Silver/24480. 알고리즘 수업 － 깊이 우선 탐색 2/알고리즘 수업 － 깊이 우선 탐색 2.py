import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n,m,r = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

for i in d:
    i.sort(reverse=True)

visited = [0]*(n+1)
visited[r] = 1
ans = [0]*(n+1)
id = 1
def dfs(x):
    global id
    ans[x] = id
    id += 1
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)
dfs(r)
print(*ans[1:],sep='\n')