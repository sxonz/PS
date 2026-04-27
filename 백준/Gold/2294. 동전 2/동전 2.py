n,k = map(int,input().split())
c = sorted([int(input()) for _ in range(n)])
m=100000000000
dp = [m]*(k+1)
for i in c:
    if i <= k:
        dp[i] = 1
for i in range(1,k+1):
    tmp = min(m,dp[i])
    for j in c:
        if i-j > 0:
            tmp = min(tmp,dp[i-j]+1)
    dp[i] = tmp
if dp[k] >= m:
    print(-1)
else:
    print(dp[k])