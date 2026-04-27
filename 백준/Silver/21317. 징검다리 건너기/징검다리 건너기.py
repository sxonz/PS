import sys
input = sys.stdin.readline
n = int(input())
stone = []
M = int(1e9)
dp = [M]*n
dp[0] = 0
for i in range(n-1):
    s, b = map(int, input().split())
    stone.append((s, b))
    if i+1<n: dp[i+1] = min(dp[i+1], dp[i]+s)
    if i+2<n: dp[i+2] = min(dp[i+2], dp[i]+b)
k =  int(input())
_min = dp[-1]
for i in range(3, n):
    e, dp1, dp2 = dp[i-3]+k, M,M
    for j in range(i, n-1):
        if i+1<=n : dp1 = min(dp1, e+stone[j][0])
        if i+2<=n : dp2 = min(dp2, e+stone[j][1])
        e, dp1, dp2 = dp1, dp2, M
    _min = min(_min, e)
print(_min)