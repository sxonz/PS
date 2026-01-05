from math import log2
n = int(input())
l = int(log2(n))+1

dp = [0]*(n+1)
dp[0] = 1
for k in range(l):
    for i in range(n+1):
        if i-2**k < 0:
            continue
        dp[i] += dp[i-2**k]
        dp[i] %= int(1e9)
print(dp[n])