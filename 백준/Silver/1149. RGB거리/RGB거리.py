n = int(input())
dp = [[0,0,0] for _ in range(n+1)]
d = []

for i in range(n):
    r,g,b = map(int,input().split())
    d.append([r,g,b])

for i in range(1,n+1):
    for j,k,l in zip([0,1,2],[2,0,1],[1,2,0]):
        dp[i][j] = min(dp[i-1][k],dp[i-1][l]) + d[i-1][j]

print(min(dp[n]))