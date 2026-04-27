n = int(input())
d = list(map(int,input().split()))
r = list(map(int,input().split()))

dp = [[[0,0,0,0,0] for _ in range(n+1)] for i in range(n+1)]
dp[1][0] = [d[0],d[0],d[0],d[0],d[0]]
for i in range(1,n):
    for j in range(1,n+1):
        if i>=j:
            dp[j][i][0] = dp[j-1][i-2][4]+d[i]
        if j > 1:
            dp[j][i][1] = dp[j-1][i-1][0] + d[i] + r[i-1]
            if j > 2 and i > 1:
                dp[j][i][2] = dp[j-1][i-1][4]+d[i]
                dp[j][i][3] = max(dp[j-1][i-1][1]-r[i-2]+r[i-1]+d[i], dp[j-1][i-1][2]+d[i]+r[i-1], dp[j-1][i-1][3]-r[i-2]+r[i-1]+d[i])
        dp[j][i][4] = max(dp[j][i-1][4],max(dp[j][i]))
for i in dp[1:]:
    print(max(max(j) for j in i))