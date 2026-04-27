n,m,k = map(int,input().split())
d = [list(input()) for i in range(n)]
psumw = [[0]*(m+1) for i in range(n+1)]
psumb = [[0]*(m+1) for i in range(n+1)]
for i in range(n):
    for j in range(m):
        psumw[i][j] = psumw[i-1][j]+psumw[i][j-1]-psumw[i-1][j-1]
        psumb[i][j] = psumb[i-1][j]+psumb[i][j-1]-psumb[i-1][j-1]
        if d[i][j] == "W":
            if (i+j)%2^1:
                psumw[i][j] += 1
            else:
                psumb[i][j] += 1
        else:
            if (i+j)%2:
                psumw[i][j] += 1
            else:
                psumb[i][j] += 1

ans = 0
for i in range(k-1,n):
    for j in range(k-1,m):
        ans = max(ans, psumw[i][j]-psumw[i-k][j]-psumw[i][j-k]+psumw[i-k][j-k])
        ans = max(ans, psumb[i][j]-psumb[i-k][j]-psumb[i][j-k]+psumb[i-k][j-k])
print(k*k-ans)