n = int(input())
d = list(map(int,input().split()))
dp = [int(1e10)]*(n+1)
dp[0] = 0
for i in range(n):
    for j in range(min(i+d[i],n)+1):
        dp[j] = min(dp[j],dp[i]+1)
if dp[n] == int(1e10) and n != 1:
    print(-1)
else:
    print(dp[n-1])