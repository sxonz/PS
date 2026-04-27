import sys
sys.setrecursionlimit(100000)
n = int(input())
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visited = [False]*(n+1)
visited[1] = True
depth = [0]*(n+1)
depth[1] = 1
parents = [0]*(n+1)

def dfs(x):
    for nx in d[x]:
        if not visited[nx]:
            parents[nx] = x
            visited[nx] = True
            depth[nx] = depth[x] + 1
            dfs(nx)

dfs(1)

m = int(input())
ans = []
for i in range(m):
    a,b = map(int,input().split())
    if depth[a] > depth[b]:
        a,b = b,a

    if depth[a] != depth[b]:
        while depth[a] != depth[b]:
            b = parents[b]
    while a != b:
        a,b = parents[a],parents[b]
    ans.append(a)
for i in ans:
    print(i)
    
