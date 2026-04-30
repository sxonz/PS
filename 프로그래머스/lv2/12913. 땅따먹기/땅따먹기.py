def solution(land):
    dp = [[0 for i in range(4)] for j in range(len(land))]
    dp[0] = land[0]
    for i in range(1,len(land)):
        for j in range(4):
            m = 0
            if j != 0:
                m = dp[i-1][0]
            if j != 1:
                m = max(m,dp[i-1][1])
            if j != 2:
                m = max(m,dp[i-1][2])
            if j != 3:
                m = max(m,dp[i-1][3])
            dp[i][j] = m + land[i][j]
    return max(dp[len(land)-1])