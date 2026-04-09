n,m = map(int,input().split())
r = list(map(int,input().split()))+[0]*m
d = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n+m):
        r[i] -= d[i][j]
        r[j] += d[i][j]
print(*r)