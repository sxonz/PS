n = int(input())
hp = [0] + list(map(int,input().split()))
joy = [0] + list(map(int,input().split()))

dp = [[0]*100 for i in range(n+1)]

for i in range(1,n+1):
    for k in range(100):
        if k-hp[i] < 0:
            dp[i][k] = dp[i-1][k]
            continue
        dp[i][k] = max(dp[i-1][k],dp[i-1][k-hp[i]] + joy[i])
print(max(dp[-1]))