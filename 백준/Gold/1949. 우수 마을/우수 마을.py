import sys
sys.setrecursionlimit(20000)
n = int(input())
r = [0]+list(map(int,input().split()))
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

dp = [[0,0,0] for i in range(n+1)]
INF = int(1e12)
def dfs(x,par):
    g = 0
    m = 0
    tmp = []
    flag = False
    for nx in d[x]:
        if nx == par:
            continue
        dfs(nx,x)
        g += max(dp[nx][1],dp[nx][2])
        m += max(dp[nx])
        if max(dp[nx]) == dp[nx][0]:
            flag = True
        else:
            tmp.append(dp[nx][0]-max(dp[nx]))

    dp[x][0] = g+r[x]
    if flag:
        dp[x][1] = m
    elif tmp:
        dp[x][1] = m+max(tmp)
    else:
        dp[x][1] = -INF
    dp[x][2] = g
dfs(1,-1)
print(max(dp[1]))
