I = lambda:map(int,input().split())
n = int(input())
d = list(I())
m = int(input())
r = list(I())
dp = [[0]*40001 for _ in range(n+1)]
res = [0]*40001
res[0] = 1
dp[0][0] = 1
for i in range(1,n+1):
    dp[i][0] = 1
    for j in range(1,40001):
        dp[i][j] |= dp[i-1][j]
        if j+d[i-1] < 40001:
            dp[i][j] |= dp[i-1][j+d[i-1]]
        if j-d[i-1] >= 0:
            dp[i][j] |= dp[i-1][j-d[i-1]]
        if d[i-1]-j >= 0:
            dp[i][j] |= dp[i-1][d[i-1]-j]
        res[j] |= dp[i][j]
for i in r:
    print("NY"[res[i]],end=' ')