import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

for test in range(int(input())):
    n,m = map(int,input().split())
    graph = [0]*(n+1)
    visited = [0]*(n+1)
    d = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
        d[b].append(a)
    
    def dfs(x,par):
        flag = True
        for nx in d[x]:
            if not visited[nx]:
                visited[nx] = True
                graph[nx] = graph[x] ^ 1
                flag &= dfs(nx,x)
            elif nx != par:
                flag &= graph[x] != graph[nx]
        return flag
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            tmp = dfs(i,-1)
            if not tmp:
                print("impossible")
                break
    else:
        print("possible")


        