n,m = map(int,input().split())
MAX = 100000
d = [[MAX] + list(map(int,input().split())) + [MAX] for i in range(n)]
dp = [[[MAX] + [0]*(m) + [MAX] for i in range(n)] for j in range(3)]
dp[0][0] = d[0][::]
dp[1][0] = d[0][::]
dp[2][0] = d[0][::]
dir = [0,1,2]
dpdir = [0,-1,1]
for i in range(1,n):
    for j in range(1,m+1):
        for k in range(3):
            dp[k][i][j] = min(dp[dir[(k+1)%3]][i-1][j+dpdir[k]],dp[dir[k-1]][i-1][j+dpdir[k]]) + d[i][j]
print(min([min(dp[k][-1]) for k in range(3)]))
