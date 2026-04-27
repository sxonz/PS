n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
dp = [[0,*t,0] for t in [[0]*_ for _ in range(1,n+1)]]
dp[0][1] = d[0][0]

for i in range(1,n):
    for j in range(1,i+2):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + d[i][j-1]    
print(max(dp[n-1]))