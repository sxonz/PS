import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(x):
    global flag
    visited[x] = True
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            check[nx] = check[x] ^ 1
            dfs(nx)
        else:
            if check[nx] == check[x]:
                flag = False


k = int(input())
for t in range(k):
    n,m = map(int,input().split())
    d = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
        d[b].append(a)

    visited = [False]*(n+1)
    check = [-1]*(n+1)
    check[1] = 1
    flag = True
    for i in range(1,n+1):
        if flag:
            dfs(i)
        else:
            break
    if flag:
        print('YES')
    else:
        print('NO')