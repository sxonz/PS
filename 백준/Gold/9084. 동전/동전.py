testcase = int(input())
ans = []
for _ in range(testcase):
    n = int(input())
    coin = list(map(int, input().split()))
    t = int(input())
    dp = [[0]*(t+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = 1
        for j in range(1,t+1):
            dp[i][j] = dp[i-1][j]
            if j-coin[i-1] >= 0:
                dp[i][j] += dp[i][j-coin[i-1]]
    ans.append(dp[n][t])
for i in ans:
    print(i)

