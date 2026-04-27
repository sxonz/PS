n = int(input())
dp = [0]*(n+1) + [int(1e9)]*10
for i in range(1,n+1):
    dp[i] = min(dp[i-1],dp[i-2],dp[i-5],dp[i-7])+1
print(dp[n])