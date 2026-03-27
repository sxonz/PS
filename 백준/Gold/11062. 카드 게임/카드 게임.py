for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    dp = [[0]*n for i in range(n)]
    for i in range(n):
        dp[i][i] = d[i]*(n%2)
    for k in range(1,n):
        for i in range(n-k):
            if (n-k)%2:
                dp[i][i+k] = max(d[i]+dp[i+1][i+k],dp[i][i+k-1]+d[i+k])
            else:
                dp[i][i+k] = min(dp[i][i+k-1],dp[i+1][i+k])
    print(dp[0][n-1])