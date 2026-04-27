n,t = map(int,input().split())
d = [tuple(map(int,input().split()))for i in range(n)]
s = sum([d[i][1]for i in range(n)])
dp = [s]*(t+1)
for i in range(n):
    for j in range(t,-1,-1):
        if j-d[i][0] < 0:
            break
        dp[j] = min(dp[j],dp[j-d[i][0]]-d[i][1])
print(dp[t])