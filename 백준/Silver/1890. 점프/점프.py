n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
dp = [[0]*n for i in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j]:
            r = d[i][j]
            if i+r < n:
                dp[i+r][j] += dp[i][j]
            if j+r < n:
                dp[i][j+r] += dp[i][j]
print(dp[n-1][n-1]//4)