testcase = int(input())
ans = []
for test in range(testcase):
    n = int(input())
    d = list(map(int,input().split()))
    m = int(input())
    dp = [0]*(m+2)
    dp[0] = 1
    for i in range(n):
        for j in range(m+1):
            if j-d[i] >= 0:
                dp[j] += dp[j-d[i]]
    ans.append(dp[m])
for i in ans:
    print(i)