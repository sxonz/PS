n,r,c = map(int,input().split())
d = [["."]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == (r+c)%2:
            d[i][j] = "v"
for i in d:
    print(''.join(i))