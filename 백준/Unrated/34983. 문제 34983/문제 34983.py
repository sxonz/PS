n,r,g = map(int,input().split())
dp = [[int(1e9)]*(g+2) for i in range(r+2)]
dp[0][0] = 0
for i in range(n):
    a,b = map(int,input().split())
    for i in range(r,-1,-1):
        for j in range(g,-1,-1):
            dp[i][j] = min(dp[i][j],dp[i+1][j],dp[i][j+1])
            if i>=a and j>=b:
                dp[i][j] = min(dp[i][j],dp[i-a][j-b]+1)
print(dp[r][g] if dp[r][g] != int(1e9) else -1)