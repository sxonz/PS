def solution(d):
    n = len(d)
    if n == 1:
        return d[0]
    dp = [[0,0] for i in range(n)]
    for i in range(n-1):
        dp[i][0] = dp[i-1][1] + d[i]
        dp[i][1] = max(dp[i-1])
    m = max(dp[n-2])
    dp = [[0,0] for i in range(n)]
    for i in range(1,n):
        dp[i][0] = dp[i-1][1] + d[i]
        dp[i][1] = max(dp[i-1])
    return max(m,max(dp[n-1]))