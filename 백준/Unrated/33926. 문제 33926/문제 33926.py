import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d =[[0]*m]+ [[0]+list(map(int,input().split()))for i in range(n)]
b =[[0]*m]+ [[0]+list(map(int,input().split()))for i in range(n)]
minarr = [[int(1e20)]*(m+1) for i in range(n+1)]
maxarr = [[-int(1e20)]*(m+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m +1):
        if i+j == 2:
            minarr[i][j] = d[i][j] * (b[i][j]*-2+1)
            maxarr[i][j] = d[i][j] * (b[i][j]*-2+1)
            continue
        if b[i][j]:
            minarr[i][j] = -(max(maxarr[i-1][j],maxarr[i][j-1])+d[i][j])
            maxarr[i][j] = -(min(minarr[i-1][j],minarr[i][j-1])+d[i][j])
        else:
            minarr[i][j] = min(minarr[i-1][j],minarr[i][j-1])+d[i][j]
            maxarr[i][j] = max(maxarr[i-1][j],maxarr[i][j-1])+d[i][j]
print(maxarr[n][m])