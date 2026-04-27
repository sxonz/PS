n = int(input())
d = list(map(int,input().split()))
dp = [[1,1] for i in range(n)]
bef = d[0]
for i in range(1,n):
    if d[i] >= bef:
        dp[i][0] = dp[i-1][0] + 1
    if d[i] <= bef:
        dp[i][1] = dp[i-1][1] + 1
    bef = d[i]
print(max([max(i) for i in dp]))