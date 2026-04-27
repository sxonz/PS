import sys
input = sys.stdin.readline
testcase = int(input())
for t in range(testcase):
    n = int(input())
    d = []
    d.append(list(map(int,input().split())))
    d.append(list(map(int,input().split())))
    dp = [[],[]]
    dp[0].append(d[0][0])
    dp[1].append(d[1][0])
    if n != 1:
        dp[0].append(dp[1][0] + d[0][1])
        dp[1].append(dp[0][0] + d[1][1])
    for i in range(2,n):
        dp[0].append(max(dp[1][i-1],dp[1][i-2]) + d[0][i])
        dp[1].append(max(dp[0][i-1],dp[0][i-2]) + d[1][i])
    print(max(dp[0][-1],dp[1][-1]))