n,m = map(int,input().split())
d = [[0]+list(map(int,input().split())) for i in range(n)]
d = [[0]*(m+1)] + d
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + d[i][j]
print(dp[n][m])
