n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
dp = [[1]*n for i in range(n)]

dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if dp[i][j]:
            continue
        if i+d[i][j] < n:
            dp[i+d[i][j]][j] = 0
        if j+d[i][j] < n:
            dp[i][j+d[i][j]] = 0
print("HHairnugH a r u"[dp[-1][-1]::2])