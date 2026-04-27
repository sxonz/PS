d = [int(input()) for _ in range(int(input()))]
dp = [0 for _ in range(100001)]
for i in range(6):
    dp[i] = (i+2)//2

for i in range(6, 100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009
for i in d:
    print(dp[i])