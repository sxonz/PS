def solution(n):
    n *= 2
    dp = [[0]*15 for i in range(n+1)]
    dp[0] = [1]+[0]*14
    for i in range(1,n+1):
        dp[i][0] = dp[i-1][1]
        dp[i][14] = dp[i-1][13]
        for j in range(1,14):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    for i in dp:
        print(i)
    return dp[n][0]