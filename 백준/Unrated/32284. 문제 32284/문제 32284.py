n,m = map(int,input().split())
x,y = map(int,input().split())

d = [['']*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i < x and j <= y:
            d[i][j] = "S"
        elif i <= x and j > y:
            d[i][j] = "W"
        elif i > x and j >= y:
            d[i][j] = "N"
        else:
            d[i][j] = "E"

for i in d:
    print(*i,sep='')