import sys
sys.setrecursionlimit(100000)

for t in range(int(input())):
    n = int(input())
    d = [0]+list(map(int,input().split()))
    
    visited = [0]*(n+1)
    proc = [0]*(n+1)
    stack = []
    cnt = n
    def dfs(x):
        global cnt
        visited[x] = 1
        stack.append(x)
        if visited[d[x]]:
            if not proc[d[x]]:
                while stack:
                    c = stack.pop()
                    cnt -= 1
                    if c == d[x]:
                        break
        else:
            dfs(d[x])
        proc[x] = 1
    
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
    print(cnt)
