import sys
input = sys.stdin.readline
N = 1001
MOD = 1000000009
dp = [[0] * N for _ in range(N)]
dp[1][1],dp[2][1],dp[2][2],dp[3][1],dp[3][2],dp[3][3] = 1,1,1,1,2,1
for i in range(4, N):
    for j in range(1, N):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD
for _ in range(int(input())):
    a,b = map(int, input().split())
    print(sum(dp[a][:b+1]) % MOD)