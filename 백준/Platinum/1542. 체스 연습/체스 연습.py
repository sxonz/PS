
n = 100
d = [[[] for i in range(n)] for j in range(n)]
g = [[-1]*n for i in range(n)]
t = [[0]*n for i in range(n)]
for i in range(n):
    t[i][0] = -1
    t[0][i] = -1
    t[i][i] = -1

for i in range(n):
    for j in range(n):
        if t[i][j] == -1:
            continue
        for k in range(2*n):
            if k not in d[i][j]:
                g[i][j] = k
                break
        for k in range(i+1,n):
            d[k][j].append(g[i][j])
        for k in range(j+1,n):
            d[i][k].append(g[i][j])
        for k in range(n):
            if i+k >= n or j+k >= n:
                break
            d[i+k][j+k].append(g[i][j])

# for i in g:
#     for j in i:
#        j = str(j)
#        j = " "*(2-len(j))+j
#        print(j,end=' ')
#     print()
for _ in range(5):
    n = int(input())
    d = [tuple(map(int,input().split())) for i in range(n)]
    res = 0
    for x,y in d:
        if t[x][y] == -1:
           res = 1
           break
        res ^= g[x][y]
    if res:
        print("S")
    else:
        print("D")