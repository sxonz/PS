import sys

input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
m = 0
for i in range(n):
    dp[i] = max(dp[i],m)
    m = dp[i]
    t,v = map(int,input().split())
    if i+t > n:
        continue
    dp[i+t] = max(dp[i+t],dp[i]+v)
print(max(dp))