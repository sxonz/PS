import sys
input = sys.stdin.readline
max_ = int(1e9)

n = int(input())
d = []

for i in range(n):
    r,g,b = map(int,input().split())
    d.append([r,g,b])

ans = []
for rgb in [0,1,2]:
    dp = [[0,0,0] for _ in range(n+1)]
    for i in range(3):
        if i == rgb:
            dp[1][i] = d[0][i]
        else:
            dp[1][i] = max_

    for i in range(2,n):
        for j,k,l in zip([0,1,2],[2,0,1],[1,2,0]):
            dp[i][j] = min(dp[i-1][k],dp[i-1][l]) + d[i-1][j]
    
    for i in range(3):
        if i == rgb:
            dp[n][i] = max_
            continue
        tmp = [1,1,1]
        tmp[i] = 0

        dp[n][i] = min([dp[n-1][j] for j in range(3) if tmp[j] == 1]) + d[n-1][i]

    ans.append(min(dp[n]))
print(min(ans))