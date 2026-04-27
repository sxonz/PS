a = input()
b = input()
n = len(a)
m = len(b)
dp = [[0]*(m+1) for _ in range(n+1)]
p = [[(0,0)]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            p[i][j] = (i-1,j-1)
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                p[i][j] = (i-1,j)
            else:
                dp[i][j] = dp[i][j-1]
                p[i][j] = (i,j-1)
print(dp[n][m])
befi,befj = n,m
i,j = p[n][m]
s = ""
while True:
    if i+1==befi and j+1==befj:
        s += a[befi-1]
    befi,befj=i,j
    if i==0 or j==0:
        break
    i,j = p[i][j]
print(s[::-1])