n,w = map(int,input().split())
dp = [[0 for i in range(w+1)] for j in range(n)]
for i in range(n):
    cur = int(input())
    for j in range(w+1):
        dp[i][j] = dp[i-1][j] + (j % 2 + 1 == cur)
    for j in range(1,w+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + (j % 2 + 1 == cur))
print(max(dp[-1]))
