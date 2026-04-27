d = [int(input()) for i in range(int(input()))]
dp = [5]*(max(d)+1)
dp[1] = 4
for i in range(2,max(d)+1):
    dp[i] = dp[i-1]*5 % 1000000007
dp[1] = 5
for i in d:
    print(dp[i])