MOD = 1000000007

testcase = int(input())
ans = []
for test in range(testcase):
    c,v,l = map(int,input().split())
    dp = [[0,0] for i in range(l+1)]
    dp[1][1] = v
    dp[1][0] = c
    for i in range(2,l+1):
        dp[i][0] = dp[i-1][1] * c % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * v % MOD
    ans.append(dp[l][1] % MOD)
for i in range(testcase):
    print(f'Case #{i+1}: {ans[i]}')