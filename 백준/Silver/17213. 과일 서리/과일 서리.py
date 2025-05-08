n = int(input())
m = int(input())
dp = [[0]*(m+1)for i in range(n+1)]
def npm(x,y):
    if y<x:return 0
    if x==1:return 1
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = npm(x,y-1) + npm(x-1,y-1)
    return dp[x][y]
print(npm(n,m))