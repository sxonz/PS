M = 100001
MOD = 1000000009
dp = [[0,0,0] for i in range(M)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4,M):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % MOD
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % MOD

for i in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % MOD)
