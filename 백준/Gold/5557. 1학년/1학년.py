n = int(input())
d = list(map(int,input().split()))

dp = [[0 for j in range(21)]for i in range(n-1)]
dp[0][d[0]] = 1
for i in range(1,n-1):
    for j in range(d[i],21):
        dp[i][j-d[i]] += dp[i-1][j]
    for j in range(0,21-d[i]):
        dp[i][j+d[i]] += dp[i-1][j]
print(dp[-1][d[-1]])
