n,m = map(int,input().split())
d = [tuple(map(int,input().split()))for i in range(m)]
dp = [0]*(n+1)
for i in range(m):
    for j in range(n,d[i][0]-1,-1):
        dp[j] = max(dp[j],dp[j-d[i][0]]+d[i][1])
print(dp[-1])
