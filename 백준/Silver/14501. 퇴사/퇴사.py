n = int(input())
d = [tuple(map(int,input().split()))for i in range(n)]
dp = [0]*(n+1)
for i in range(n):
    dp[i] = max(dp[i],dp[i-1])
    if i + d[i][0] > n:
        continue
    dp[i+d[i][0]] = max(dp[i+d[i][0]],dp[i]+d[i][1])
print(max(dp[n],dp[n-1]))