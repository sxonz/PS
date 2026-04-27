n = int(input())
d = {2:3}
for i in range(4,31,2):
    d[i] = 2
dp = [[0]*32 for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    if i%2:continue
    for j in d:
        if i-j >= 0:
            dp[i][j] += sum(dp[i-j])*d[j]
        else:
            break
print(sum(dp[n]) if n else 1)