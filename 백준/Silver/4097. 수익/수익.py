while True:
    n = int(input())
    if n == 0:
        break
    d = [int(input())for i in range(n)]
    dp = [0]*n
    for i in range(n):
        dp[i] = max(dp[i-1],0) + d[i]
    print(max(dp))