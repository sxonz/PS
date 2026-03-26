n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
INF = int(1e12)
dp = [[[INF,INF,INF] for i in range(m)] for j in range(n)]
for i in range(m):
    dp[0][i] = [d[0][i],d[0][i],d[0][i]]

for i in range(1,n):
    dp[i][0] = [INF,dp[i-1][0][2]+d[i][0],min(dp[i-1][1][0],dp[i-1][1][1])+d[i][0]]
    for j in range(1,m-1):
        dp[i][j] = [min(dp[i-1][j-1][1],dp[i-1][j-1][2])+d[i][j],min(dp[i-1][j][0],dp[i-1][j][2])+d[i][j],min(dp[i-1][j+1][0],dp[i-1][j+1][1])+d[i][j]]
    dp[i][-1] = [min(dp[i-1][-2][1],dp[i-1][-2][2])+d[i][-1],dp[i-1][-1][0]+d[i][-1],INF]
print(min([min(i) for i in dp[-1]]))