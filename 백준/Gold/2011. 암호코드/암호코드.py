n = input()
l = len(n)
dp = [0]*(l+1)
dp[0] = 1 if n[0] != "0" else 0
dp[-1] = 1
for i in range(1,l):
    dp[i] = dp[i-1] if n[i] != "0" else 0
    if 10 <= int(n[i-1:i+1]) <= 26:
        dp[i] += dp[i-2]
print(dp[-2]%1000000)