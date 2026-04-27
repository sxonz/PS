h,y = map(int,input().split())
dp = [0]*(y+1)
dp[0] = h
for i in range(1,y+1):
    if i>=5:
        dp[i] = max(dp[i-1]*105, dp[i-3]*120, dp[i-5]*135)
    elif i>=3:
        dp[i] = max(dp[i-1]*105, dp[i-3]*120)
    else:
        dp[i] = dp[i-1]*105
    dp[i] = dp[i] // 100
print(dp[y])