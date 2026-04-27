n,m = map(int,input().split())
a = input()
b = input()
dp = [[-1]*(n+2) for i in range(m)]
for i in range(1,n+1):
    if a[i-1] == b[0]:
        dp[0][i] = 1
    else:
        dp[0][i] = 0
for i in range(1,m):
    for j in range(1,n+1):
        if dp[i-1][j-1] == -1 and dp[i-1][j+1] == -1:
            continue
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j+1]) + (b[i] == a[j-1])
print(max(dp[-1]))