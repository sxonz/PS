n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
dp = [[[int(1e9),-int(1e9)] for i in range(3)] for j in range(n)]
for i in range(3):
    dp[0][i] = [d[0][i],d[0][i]]
for i in range(1,n):
    dp[i][0] = [min(dp[i-1][0][0],dp[i-1][1][0])+d[i][0],max(dp[i-1][0][1],dp[i-1][1][1])+d[i][0]]
    dp[i][1] = [min(dp[i-1][0][0],dp[i-1][1][0],dp[i-1][2][0])+d[i][1],max(dp[i-1][0][1],dp[i-1][1][1],dp[i-1][2][1])+d[i][1]]
    dp[i][2] = [min(dp[i-1][1][0],dp[i-1][2][0])+d[i][2],max(dp[i-1][1][1],dp[i-1][2][1])+d[i][2]]
print(max(dp[-1][0][1],dp[-1][1][1],dp[-1][2][1]),min(dp[-1][0][0],dp[-1][1][0],dp[-1][2][0]))
