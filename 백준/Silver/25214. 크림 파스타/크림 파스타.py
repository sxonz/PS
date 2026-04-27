n = int(input())
d = list(map(int,input().split()))
dp = d[::]
dp[0] = 0
m = d[0]
for i in range(1,n):
    m = min(m,d[i])
    dp[i] = max(d[i] - m,dp[i-1])
print(*dp)