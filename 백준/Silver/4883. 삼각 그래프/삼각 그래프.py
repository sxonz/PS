t = 1
while True:
    n = int(input())
    if not n:
        break
    d = [list(map(int,input().split())) for i in range(n)]
    dp = [[0,0,0] for i in range(n)]
    dp[0] = [int(1e9),d[0][1],d[0][1]+d[0][2]]

    for i in range(1,n):
        dp[i][0] = min(dp[i-1][0],dp[i-1][1])+d[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][1],dp[i-1][2],dp[i][0])+d[i][1]
        dp[i][2] = min(dp[i-1][1],dp[i-1][2],dp[i][1])+d[i][2]
    print(f"{t}. {dp[-1][1]}")
    t += 1

