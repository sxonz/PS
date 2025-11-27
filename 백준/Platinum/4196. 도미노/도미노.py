import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

for t in range(int(input())):
    n,m = map(int,input().split())
    d = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
    scc = [0]*(n+1)
    cur = 1
    stack = []
    parents = [int(1e9)]*(n+1)

    visited = [0]*(n+1)
    proc = [0]*(n+1)
    id = 0
    ids = [0]*(n+1)
    def dfs(x):
        global id
        global cur

        visited[x] = True
        stack.append(x)
        parents[x] = id
        ids[x] = id
        id += 1

        for nx in d[x]:
            if not visited[nx]:
                dfs(nx)
            if not proc[nx]:
                parents[x] = min(parents[x],parents[nx])
        if parents[x] == ids[x]:
            while stack:
                tmp = stack.pop()
                scc[tmp] = cur
                proc[tmp] = 1
                if tmp == x:
                    break
            cur += 1
    
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)

    res = cur-1
    indegree = [0]*cur
    for i in range(1,n+1):
        for j in d[i]:
            if scc[i] != scc[j]:
                if not indegree[scc[j]]:
                    res -= 1
                indegree[scc[j]] += 1
    print(res)
    
