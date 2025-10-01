while True:
    n = int(input())
    if not n:
        break
    dp = [[0]*(n+1) for i in range(2*n+1)]
    dp[0][0] = 1
    for i in range(1,2*n+1):
        dp[i][0] = dp[i-1][1]
        for j in range(1,n):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][n] = dp[i-1][n-1]
    print(dp[n*2][0])