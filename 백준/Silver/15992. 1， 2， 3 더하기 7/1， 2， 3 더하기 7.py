N = 1000
dp = [[0] * (N+1) for _ in range(N+1)]
MOD= 1000000009
dp[1][1] = dp[2][1] = dp[3][1] = 1

for i in range(2, N+1):
    for j in range(1, N+1):
        for k in range(1, 4):
            if j - k > 0 :
                dp[j][i] += dp[j-k][i-1]
            dp[j][i] %= MOD
for _ in range(int(input())):
    n, m = map(int,input().split())
    print(dp[n][m])