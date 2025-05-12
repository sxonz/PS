n,m = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(n)]
dp = [0]*(m+1)
for i in range(n):
    for j in range(m,-1,-1):
        if j-d[i][0] < 0:
            break
        dp[j] = max(dp[j],dp[j-d[i][0]]+d[i][1])
print(dp[m])