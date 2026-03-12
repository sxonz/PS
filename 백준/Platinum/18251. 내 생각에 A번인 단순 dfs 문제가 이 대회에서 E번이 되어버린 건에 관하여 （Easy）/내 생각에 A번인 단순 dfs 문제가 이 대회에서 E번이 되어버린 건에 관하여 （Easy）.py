import sys
sys.setrecursionlimit(200000)
from math import *

n = int(input())
h = int(log2(n))+1
d = [0] + list(map(int,input().split()))

r = [[0]*(n+1) for i in range(h)]
pos = [[0]*(n+1) for i in range(h)]
cur = 0
def dfs(idx,x,depth):
    global cur
    if idx*2 <= n:
        dfs(idx*2,d[idx*2],depth-1)
    r[depth][cur] = x
    pos[depth][cur] = 1
    cur += 1
    if idx*2+1 <= n:
        dfs(idx*2+1,d[idx*2+1],depth-1)
dfs(1,d[1],h-1)
psum = [[0]*(n+1) for i in range(h+1)]
s = [[0]*(n+1) for i in range(h+1)]
for i in range(1,h+1):
    for j in range(n):
        psum[i][j] = psum[i-1][j]+r[i-1][j]
        s[i][j] = s[i-1][j]+pos[i-1][j]

ans = -int(1e9)
dp = [-int(1e9)]*n
for i in range(1,h+1):
    for j in range(i,h+1):
        tmp = [psum[j][k]-psum[i-1][k] for k in range(n) if s[j][k]-s[i-1][k]]
        l = len(tmp)
        for k in range(l):
            dp[k] = max(dp[k-1]+tmp[k], tmp[k])
        if dp:
            ans = max(ans,max(dp))
            for k in range(l):
                dp[k] = -int(1e9)
print(ans)