n,k = map(int,input().split())
d = [int(input()) for i in range(n)]
dp = [0]*(k+1)
dp[0] = 1
for i in d:
    for j in range(k):
        if i+j <= k:
            dp[i+j] += dp[j]
print(dp[k])