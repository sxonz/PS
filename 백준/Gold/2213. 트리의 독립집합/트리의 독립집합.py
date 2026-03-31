import sys
sys.setrecursionlimit(20000)

INF = int(1e12)

n = int(input())
r = [0] + list(map(int,input().split()))
d = [[] for i in range(n+1)]
path = [[] for i in range(n+1)]
l = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
    path[a].append([0,0,0])
    path[b].append([0,0,0])
    l[a] += 1
    l[b] += 1

dp = [[0,0,0] for i in range(n+1)]
def dfs(x,par):
    flag = False
    tmp = []
    dp[x][0] = r[x]
    k = 0
    for nx,p,i in zip(d[x],path[x],range(l[x])):
        if nx == par:
            continue
        dfs(nx,x)
        if dp[nx][1] > dp[nx][2]:
            dp[x][0] += dp[nx][1]
            dp[x][2] += dp[nx][1]
            p[0] = 1
            p[2] = 1
        else:
            dp[x][0] += dp[nx][2]
            dp[x][2] += dp[nx][2]
            p[0] = 2
            p[2] = 2
        m = max(dp[nx])
        k += m
        if dp[nx][0] == m:
            p[1] = 0
            flag = True
        elif dp[nx][1] == m:
            p[1] = 1
            tmp.append((dp[nx][0]-m,i))
        else:
            p[1] = 2
            tmp.append((dp[nx][0]-m,i))
    if flag:
        dp[x][1] = k
    elif tmp:
        path[x][max(tmp)[1]][1] = 0
        dp[x][1] = k+max(tmp)[0]
    else:
        dp[x][1] = -INF
dfs(1,0)
ans = []
def back(x,par,cur):
    if cur == 0:
        ans.append(x)
    for nx,p in zip(d[x],path[x]):
        if nx == par:
            continue
        back(nx,x,p[cur])
res = max(dp[1])
back(1,0,dp[1].index(res))
print(res)
ans.sort()
print(*ans)