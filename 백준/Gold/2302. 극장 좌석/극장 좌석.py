n = int(input())
m = int(input())
d = set([int(input()) for i in range(m)])

dp = [[0,0,0] for i in range(n+1)]
dp[0] = [0,1,0]
for i in range(1,n+1):
    if i-1 not in d and i not in d:
        dp[i][0] = dp[i-1][2]
    dp[i][1] = dp[i-1][1] + dp[i-1][0]
    if i+1 <= n and i+1 not in d and i not in d:
        dp[i][2] = dp[i-1][1] + dp[i-1][0]
print(sum(dp[n]))
