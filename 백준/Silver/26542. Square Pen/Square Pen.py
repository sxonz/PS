testcase = int(input())
ans = []
for test in range(testcase):
    n = int(input())
    d = ['#'*(n+1)] + ['#' + input() for i in range(n)]
    dp = [[0]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][j] == '.':
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
    ans.append(max([max(i) for i in dp])**2)
for i in ans:
    print(i)