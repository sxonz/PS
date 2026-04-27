n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = sum([j*k for j,k in zip(dp[:i],dp[:i][::-1])])
print(dp[n])