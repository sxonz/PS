import sys
sys.setrecursionlimit(200000)

n,m = map(int,input().split())
c = [-1]*(n+1)

parents = list(range(n+1))
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

graph = [set() for i in range(n+1)]
for i in range(m):
    q,a,b = map(int,input().split())
    if q == 2:
        graph[a].add(b)
        graph[b].add(a)
    else:
        while a<b:
            if a not in graph[b]:
                union(a,b)
            a += 1
            b -= 1
else:
    pass

for i in range(1,n+1):
    graph[find(i)] |= set([find(j) for j in graph[i]])
nums = list(set(parents[1:]))
visited = [0]*(n+1)
ab = [0]*(n+1)

def dfs(x):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = 1
            ab[nx] = ab[x]^1
            dfs(nx)
        else:
            if ab[x] == ab[nx]:
                print("No")
                exit()
for i in nums:
    visited[i] = 1
    dfs(i)

print("Yes")
for i in ab[1:]:
    print("A" if i else "B",end='')
