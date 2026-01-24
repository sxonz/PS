n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
dp = [[0]*1001 for i in range(n)]
for i,v in enumerate(d):
    l,r = v
    for j in range(1001):
        dp[i][j] = min(dp[i-1][max(0,j-1)],dp[i-1][j],dp[i-1][min(j+1,1000)])
        if not l<=j<=r:
            dp[i][j] += 1
if min(dp[-1]) <= 1:
    print("World Champion")
else:
    print("Surrender")