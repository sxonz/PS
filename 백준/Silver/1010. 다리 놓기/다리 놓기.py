for t in range(int(input())):
    n,m = map(int,input().split())
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1] = list(range(m+1))
    for i in range(2,n+1):
        for j in range(i,m+1):
            dp[i][j] = sum(dp[i-1][:j])
    print(dp[n][m])