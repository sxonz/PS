n,m = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(n)]
dp = [0]*(m+2)
for i in range(n):
    for j in range(m,-1,-1):
        if j-d[i][0] < 0:
            dp[j] = max(dp[j],dp[j-1])
        else:
            dp[j] = max(dp[j],dp[j-1],dp[j-d[i][0]]+d[i][1])
print(max(dp))