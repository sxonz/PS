dp = [1]+[0]*250
for i in range(1,251):
    dp[i] = dp[i-2]*2 + dp[i-1]
try:
    while True:
        n = int(input())
        print(dp[n])
except:
    exit()
    sus