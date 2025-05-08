dp = [0]*10001
dp[0] = 1
n,m = map(int,input().split())
for i in range(1,n+1):
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007
print(dp[n])