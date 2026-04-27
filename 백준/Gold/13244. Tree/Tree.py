testcase = int(input())
ans = []
for test in range(testcase):
    n,m = int(input()),int(input())
    d = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
        d[b].append(a)
    if n-1-m:
        ans.append("graph")
        continue
    p = list(range(n+1))
    visited = [False]*(n+1)
    def F(x):
        if x-p[x]:p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b
    graph = False
    def dfs(x):
        for nx in d[x]:
            if not visited[nx]:
                visited[nx] = True
                if F(x) == F(nx):
                    graph = True
                else:
                    U(x,nx)
                    dfs(nx)
    visited[1] = True
    dfs(1)
    for i in range(1,n+1):
        if not visited[i]:
            graph = True
    if graph:
        ans.append("graph")
    else:
        ans.append("tree")
for i in ans:
    print(i)