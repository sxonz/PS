n = int(input())
dp = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if(i%2)^1:
        dp[i] = min(dp[i],dp[i//2]+1)
    if not i%3:
        dp[i] = min(dp[i],dp[i//3]+1)
print(dp[n])
res = [n]
now = n
cur = dp[n] - 1
for i in range(n, 0, -1):
    if dp[i] == cur and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        res.append(i)
        cur -= 1
print(*res)