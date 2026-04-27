d = [list(map(int,input().split())) for _ in range(9)]
m,a,b = -1,0,0
for i in range(9):
    for j in range(9):
        if d[i][j] > m:
            m = d[i][j]
            a,b=i+1,j+1
print(m)
print(a,b)