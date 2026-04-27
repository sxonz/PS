n = int(input())
d = list(map(int,input().split()))
dp = [0]*(n+1)
for i in range(n-1,-1,-1):
    if i+d[i] >= n:
        dp[i] = 1
    else:
        dp[i] = dp[i+d[i]+1] + 1

print(*dp[:-1])