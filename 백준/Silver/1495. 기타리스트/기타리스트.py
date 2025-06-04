n,s,m = map(int,input().split())
d = [0] + list(map(int,input().split()))
dp = [[0]*(m+1) for i in range(n+1)]
dp[0][s] = 1
for i in range(1,n+1):
    for k in range(m+1):
        if k-d[i] >= 0:
            dp[i][k] |= dp[i-1][k-d[i]]
        if k+d[i] <= m:
            dp[i][k] |= dp[i-1][k+d[i]]
for i in range(m,-1,-1):
    if dp[-1][i]:
        print(i)
        break
else:
    print(-1)