r,c,w = map(int,input().split())
n = r+w
dp = [[0]*(i+2) for i in range(1,n+1)]
dp[0][1] = 1
ans = 0
for i in range(1,n):
    for j in range(1,i+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        if i >= r and j >= c and j <= c+i-r:
            ans += dp[i][j]
print(ans)