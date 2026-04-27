import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
for t in range(int(input())):
    n,m = map(int,input().split())
    d = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
    
    scc = []
    curcc = 0
    visited = [0]*n
    proc = [-1]*n
    id = 1
    stack = []

    def dfs(x):
        global id,curcc
        visited[x] = id
        parent = id
        id += 1
        stack.append(x)

        for nx in d[x]:
            if not visited[nx]:
                parent = min(parent, dfs(nx))
            elif proc[nx] == -1:
                parent = min(parent, visited[nx])
        
        if parent == visited[x]:
            tmp = []
            cur = -1
            while cur != x:
                cur = stack.pop()
                proc[cur] = curcc
                tmp += [cur]
            scc.append(tmp)
            curcc += 1
        
        return parent
    
    for i in range(n):
        if not visited[i]:
            dfs(i)

    dag = [0]*curcc
    for i in range(n):
        for j in d[i]:
            if proc[i] != proc[j]:
                dag[proc[j]] += 1
    if dag.count(0) != 1:
        print("Confused")
    else:
        for i in sorted(scc[dag.index(0)]):
            print(i)
    input()
    print()
