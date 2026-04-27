m,n = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for i in range(n)]

for i in range(n):
    dp[i][0] = d[i][0]
for day in range(1,m):
    for i in range(n):
        happy = 0
        for j in range(n):
            nohappy = 2 if i == j else 1
            dp[i][day] = max(dp[i][day],dp[j][day-1]+d[i][day]//nohappy)
print(max([dp[i][m-1] for i in range(n)]))