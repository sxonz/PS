import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,r,q = map(int,input().split())
d = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
def dfs(x,child):
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            child += dfs(nx,1)
    subtree[x] = child
    return child
subtree = [0]*(n+1)
visited = [False]*(n+1)
visited[r] = True
dfs(r,1)
for i in range(q):
    u = int(input())
    print(subtree[u])