import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))
dp = [[0]*n for i in range(n)]
for i in range(1,n):
    dp[i][i-1] = 1
    
for i in range(n-1,-1,-1):
    dp[i][i] = 1
    for j in range(i+1,n):
        if d[i] == d[j]:
            dp[i][j] = dp[i+1][j-1]
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])

