n = int(input())
dp = [1]*(abs(n)+1)
if n>0:
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000000
    print(1)
    print(dp[n])
elif n<0:
    for i in range(3,abs(n)+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000000
    if n % 2:
        print(1)
        print(dp[abs(n)])
    else:
        print(-1)
        print(dp[abs(n)])
else:
    dp[n] = 0
if not dp[n]:
    print(0)
    print(0)