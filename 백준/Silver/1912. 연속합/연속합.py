n = int(input())
d = list(map(int,input().split()))
dp = [0]*n
dp[0] = d[0]

for i in range(1,n):
    if dp[i-1] < 0:
        dp[i] = d[i]
    else:
        dp[i] = dp[i-1]+d[i]
print(max(dp))
