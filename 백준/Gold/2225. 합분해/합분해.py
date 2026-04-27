n,k = map(int,input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,k+1):
    for j in range(0,n+1):
        if i == 1:
            dp[j][i] = 1
            continue
        for m in range(0,j+1):
            dp[j][i] += dp[j-m][i-1]

print(dp[n][k] % 1000000000)