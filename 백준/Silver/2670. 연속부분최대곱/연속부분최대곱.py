n = int(input())
d = [float(input()) for _ in range(n)]
dp = [0]*n
dp[0] = d[0]
for i in range(1,n):
    dp[i] = max(dp[i-1],1)*d[i]
res = str(round(max(dp)*1000)/1000)
res += (4 - len(res) + res.find('.')) * '0'
print(res)