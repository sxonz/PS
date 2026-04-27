n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
dp = [[0]*6 for i in range(n)]
for i in range(n):
    for j in range(1,6):
        if j in d[i]:
            dp[i][j] = dp[i-1][j] + 1
m,g = 0,0
for i in dp:
    if max(i) == m:
        g = min(g,i.index(m))
    if max(i) > m:
        m = max(i)
        g = i.index(m)
print(m,g)