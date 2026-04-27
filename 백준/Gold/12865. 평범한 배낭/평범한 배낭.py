n,v = map(int,input().split())

d = [(0,0)]
for _ in range(n):
    a,b = map(int,input().split())
    d.append((a,b))

dp = [[0]*(v+1) for _ in range(n+1)]
for i in range(1,n+1):
    w,p = d[i]
    for j in range(1,v+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j-w]+p,dp[i-1][j])
m = 0
for i in dp:
    m = max(m,max(i))
print(m)