from collections import deque
import sys
sys.setrecursionlimit(10000)
n,q = map(int,input().split())
num = [0] + list(map(int,input().split()))
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

r = 1
visited = [False]*(n+1)
visited[r] = True
depth = [0]*(n+1)
depth[r] = 1
parents = [0]*(n+1)
def dfs(x):
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            parents[nx] = x
            depth[nx] = depth[x] + 1
            dfs(nx)
dfs(r)

def lca(a,b):
    ra,rb = [],deque([])
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            ra.append(num[a])
            a = parents[a]
        else:
            rb.appendleft(num[b])
            b = parents[b]
    
    while a != b:
        ra.append(num[a])
        rb.appendleft(num[b])
        a,b = parents[a],parents[b]
    ra.append(num[a])
    res = ''
    for i in ra:
        res += str(i)
    for i in rb:
        res += str(i)
    res = int(res) % 1000000007
    return res

ans = []
for i in range(q):
    a,b = map(int,input().split())
    ans.append(lca(a,b))
for i in ans:
    print(i)