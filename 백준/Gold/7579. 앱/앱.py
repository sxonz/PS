n,m = map(int,input().split())

c = list(map(int,input().split()))
v = list(map(int,input().split()))
c.insert(0,0)
v.insert(0,0)
s = sum(v)
dp = [[0]*(s+1) for _ in range(n+1)]
for i in range(1,n+1):
    w = v[i]
    p = c[i]
    for j in range(0,s+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w]+p,dp[i-1][j])
dp = list(map(list,zip(*dp)))
for i in range(len(dp)):
    for j in dp[i]:
        if j >= m:
            print(i)
            break
    else:
        continue
    break