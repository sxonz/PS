n,m = map(int,input().split())
d = list(map(int,input().split()))

r = []
for i in range(m):
    r.append(d[i])
    for j in range(i+1,m):
        r.append(d[i]+d[j])
r = list(set(r))
l = len(r)
dp = [int(1e9)]*(n+1)
dp[0] = 0
for i in range(l):
    for j in range(r[i],n+1):
        if j-r[i]>=0 and dp[j-r[i]] != int(1e9):
            dp[j] = min(dp[j], dp[j-r[i]]+1)
print(dp[n] if dp[n] != int(1e9) else -1)