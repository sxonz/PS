testcase = int(input())
d = [int(input()) for _ in range(testcase)]
dp = [1,1,2]
for i in range(3,max(d)+1):
    dp += [(dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009]
for i in d:
    print(dp[i])
