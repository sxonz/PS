n = int(input())
dp = [[0]*5 for i in range(n+1)]
dp[1][3] = 1
for i in range(2,n+1):
    dp[i][4] = (i%2^1) *sum(dp[i-1])
    dp[i][3] = dp[i-1][4] + i%2 * sum(dp[i-1])
    dp[i][2] = dp[i-1][3]
    dp[i][1] = dp[i-1][2]
print(sum(dp[n]))
