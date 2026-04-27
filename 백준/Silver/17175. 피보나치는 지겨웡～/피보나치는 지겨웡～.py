n = int(input())
MOD = 1000000007
dp = [1,1]
for i in range(n-1):
    dp.append((dp[-1]+dp[-2]+1)%MOD)
print(dp[n])