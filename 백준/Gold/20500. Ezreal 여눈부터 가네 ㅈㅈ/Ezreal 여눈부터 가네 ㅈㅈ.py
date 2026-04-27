n = int(input())
dp = [[0]*15 for i in range(n+1)]
dp[0][0] = 1
MOD = 1000000007
for i in range(1,n+1):
    for j in range(15):
        dp[i][j] = (dp[i-1][(j+10**(i-1))%15] + dp[i-1][(j+10**(i-1)*5)%15]) % MOD
print(dp[n][0])