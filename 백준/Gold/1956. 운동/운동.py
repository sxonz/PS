from heapq import *

n,m = map(int,input().split())
INF = int(1e12)
d = [[INF]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a][b] = c

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if d[i][k] != INF and d[k][j] != INF:
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
ans = INF
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            if d[i][j] != INF and d[j][i] != INF:
                ans = min(ans,d[i][j]+d[j][i])
print(ans if ans != INF else -1)