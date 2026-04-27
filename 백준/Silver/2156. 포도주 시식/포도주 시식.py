n = int(input())
d = [int(input()) for i in range(n)]
dp = [[0,0] for i in range(n)]
dp[0][0] = d[0]
m = 0
for i in range(1,n):
    dp[i][0] = m+d[i]
    dp[i][1] = dp[i-1][0]+d[i]
    m = max(m,dp[i-1][0],dp[i-1][1])
print(max([max(i) for i in dp]))