import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)

parents = [int(1e9)]*(n+1)
stack = []
scc = []

visited = [0]*(n+1)
id = 0
ids = [0]*(n+1)
proc = [0]*(n+1)
def dfs(x):
    global id
    stack.append(x)
    parents[x] = id
    ids[x] = id
    id += 1
    visited[x] = 1
    for nx in d[x]:
        if parents[nx] < parents[x] and not proc[nx]:
            parents[x] = parents[nx]
        else:
            if not visited[nx]:
                dfs(nx)
                if parents[nx] < parents[x]:
                    parents[x] = parents[nx]
    if parents[x] == ids[x]:
        tmp = []
        while stack:
            c = stack.pop()
            proc[c] = 1
            tmp.append(c)
            if c == x:
                break
        scc.append(tmp)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

print(len(scc))
scc.sort(key = lambda x:min(x))
for i in scc:
    i.sort()
    print(*i,-1)