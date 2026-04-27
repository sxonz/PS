n,k = map(int,input().split())
d = list(map(int,input().split()))
dp = [0]+[int(1e9)]*k
for i in range(n):
    for j in range(k,-1,-1):
        if j-d[i] >= 0:
            dp[j] = min(dp[j],dp[j-d[i]]+1)
print(dp[k] if dp[k] != int(1e9) else -1)