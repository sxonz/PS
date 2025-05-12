n,k = map(int,input().split())
d = [tuple(map(int,input().split()))for i in range(k)]
dp = [0]*(n+1)
for i in range(k):
    for j in range(n,-1,-1):
        if j-d[i][1] >= 0:
            dp[j] = max(dp[j],dp[j-d[i][1]]+d[i][0])
print(max(dp))