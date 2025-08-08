MOD = 1000000000

n = int(input())
dp = [[[0]*(10) for i in range(n+1)] for j in range(1024)]
for i in range(1,10):
    dp[1<<i][0][i] = 1

for i in range(n):
    for k in range(1024):
        dp[k|2][i+1][1] += dp[k][i][0] % MOD
    for j in range(1,9):
        for k in range(1024):
            dp[k|(1<<(j+1))][i+1][j+1] += dp[k][i][j] % MOD
            dp[k|(1<<(j-1))][i+1][j-1] += dp[k][i][j] % MOD
    for k in range(1024):
        dp[k|(1<<8)][i+1][8] += dp[k][i][9] % MOD


print(sum(dp[1023][n-1])%MOD)