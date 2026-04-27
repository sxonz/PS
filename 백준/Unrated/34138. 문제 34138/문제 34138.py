n,m = map(int,input().split())
d = [input() for i in range(n)]

dp = [[0]*m for i in range(n)]
house = [0]*(min(n,m)+1)
for i in range(n):
    dp[i][0] = d[i][0] == "X"
    house[1] += d[i][0] == "X"
for j in range(1,m):
    dp[0][j] = d[0][j] == "X"
    house[1] += d[0][j] == "X"

for i in range(1,n):
    for j in range(1,m):
        if d[i][j] == '.':
            continue
        for k in range(1,dp[i-1][j-1]+1):
            if dp[i-k][j] or dp[i][j-k]:
                dp[i][j] = k
                break
        else:
            dp[i][j] = dp[i-1][j-1] + 1

        house[dp[i][j]] += 1

for i in range(min(n,m)-1,0,-1):
    house[i] += house[i+1]
for i in house[1:]:
    print(i)