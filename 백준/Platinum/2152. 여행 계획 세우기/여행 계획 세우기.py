import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

n,m,s,t = map(int,input().split())
edges = [tuple(map(int,input().split())) for i in range(m)]
d = [[] for i in range(n+1)]
for a,b in edges:
    d[a].append(b)

id = 1
ids = [0]*(n+1)
parents = [0]*(n+1)
stack = []

scc = [0]*(n+1)
cur = 1
visited = [0]*(n+1)
proc = [0]*(n+1)
def dfs(x):
    global id,cur
    ids[x] = id
    parents[x] = id
    id += 1
    stack.append(x)
    
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            parents[x] = min(parents[x],dfs(nx))
        elif not proc[nx]:
            parents[x] = min(parents[x],parents[nx])
    if parents[x] == ids[x]:
        tmp = -1
        while x != tmp:
            tmp = stack.pop()
            scc[tmp] = cur
            proc[tmp] = 1
        cur += 1
    return parents[x]

for i in range(1,n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)

cnt = [0]*(cur+1)
for i in scc:
    cnt[i] += 1
s,t = scc[s],scc[t]
graph = [[] for i in range(cur)]
for a,b in edges:
    if scc[a] != scc[b]:
        graph[scc[a]].append(scc[b])

visit = [0]*cur
can = [0]*cur
def path(x):
    if visit[x]:
        return can[x]
    visit[x] = 1
    if x == t:
        can[t] = cnt[t]
        return can[t]
    tmp = 0
    for nx in graph[x]:
        tmp = max(tmp,path(nx))
    if tmp:
        can[x] = tmp+cnt[x]
    return can[x]
print(path(s))
