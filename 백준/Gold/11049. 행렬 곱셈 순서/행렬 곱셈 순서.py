n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
INF = int(1e12)
dp = [[INF]*n for i in range(n)]
for i in range(n):
    dp[i][i] = 0
for k in range(1,n):
    for i in range(n-k):
        for m in range(i,i+k):
            dp[i][i+k] = min(dp[i][i+k],dp[i][m]+dp[m+1][i+k]+d[i][0]*d[m][1]*d[i+k][1])
print(dp[0][n-1])