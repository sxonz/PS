import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

n,m = map(int,input().split())
s,e = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(m)]
d.sort(key = lambda x:-x[2])

parent = list(range(n+1))
def F(x):
    if x != parent[x]:
        parent[x] = F(parent[x])
    return parent[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

graph = [[] for i in range(n+1)]
for a,b,c in d:
    if F(a) != F(b):
        U(a,b)
        graph[a].append((b,c))
        graph[b].append((a,c))

visited = [False]*(n+1)
def dfs(x):
    if x == e:
        return int(1e20)
    for nx,c in graph[x]: 
        if not visited[nx]:
            visited[nx] = True 
            tmp = dfs(nx)
            if tmp:
                return min(tmp,c)
    return 0
visited[s] = True
print(dfs(s))