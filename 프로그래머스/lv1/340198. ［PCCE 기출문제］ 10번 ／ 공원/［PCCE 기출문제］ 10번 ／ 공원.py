def solution(mats, park):
    dp = [[0 for i in range(len(park[0]))] for j in range(len(park))]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if i == 0:
                dp[i][j] = 1 if park[i][j] == "-1" else 0
                continue
            if j == 0:
                dp[i][j] = 1 if park[i][j] == "-1" else 0
                continue
            if park[i][j] == "-1":
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
    m = 0
    for i in range(len(dp)):
        m = max(m,max(dp[i]))
    ans = -1
    for i in sorted(mats):
        if i <= m:
            ans = i
    return ans
        
    answer = 0
    return answer