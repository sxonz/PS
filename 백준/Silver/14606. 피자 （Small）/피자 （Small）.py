n = int(input())
dp = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = max([dp[j] + dp[i-j] + j*(i-j) for j in range(i//2+1)])
print(dp[n])