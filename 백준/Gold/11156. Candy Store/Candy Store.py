mod = 65537
testcase = int(input())
for _ in range(testcase):
    n, c = map(int, input().split())
    d = list(map(int, input().split()))
    max_sum = sum(d)
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    for cost in d:
        for j in range(max_sum, cost - 1, -1):
            dp[j] = (dp[j] + dp[j - cost]) % mod
    ans = sum(dp[c:]) % mod
    print(ans)
