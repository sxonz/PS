n = int(input())
d = list(map(int,input().split()))
dp = [0]*(n+1)
for i in range(1,n+1):
    for j in range(i,n+1):
        dp[j] = max(dp[j],dp[j-i]+d[i-1])
print(dp[-1])