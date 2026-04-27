n = int(input())
d = [int(input()) for _ in range(n)]
dp = [[0,0] for _ in range(n+1)]
dp[1][0] = d[0]
dp[1][1] = d[0]

for i in range(2,n+1):
    dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + d[i-1]
    dp[i][1] = dp[i-1][0] + d[i-1]
print(max(dp[n]))