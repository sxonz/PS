n = int(input())
d = [[0]*n for i in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(n):
        if i+1<n:
            d[i+1][j] += d[i][j]
        if j+1<n:
            d[i][j+1] += d[i][j]
print(sum([sum(i) for i in d])+1,n*n)