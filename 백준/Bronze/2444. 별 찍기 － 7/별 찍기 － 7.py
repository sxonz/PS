n = int(input())
l = 2*n-1
d = [[" " for i in range(l)] for j in range(l)]

m = n-1
for i in range(n):
    d[i][m] = '*'
    for j in range(1,i+1):
        d[i][m+j] = '*'
        d[i][m-j] = '*'
    for k in range(l-(m+i)-1):
        d[i].pop()
    d[l-i-1] = d[i]
for i in d:
    print(''.join(i))
