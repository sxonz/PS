n,k = map(int,input().split())
fast = [[] for i in range(20001)]
for i in range(n):
    s,e,c = map(int,input().split())
    fast[s].append((e,c))
dp = [int(1e9)]*20001
dp[0] = 0
for i in range(k):
    dp[i+1] = min(dp[i]+1, dp[i+1])
    for nx,c in fast[i]:
        dp[nx] = min(dp[nx],dp[i]+c)
print(dp[k])
    