def matrixMultiple(n,A,B):
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            r = 0
            for k in range(n):
                r = (r + A[i][k]*B[k][j]) % 1000
            C[i][j] = r
    return C
            
def matrixPower(n,A,b):
    if b == 1:
        return A
    if b == 2:
        return matrixMultiple(n,A,A)
    r = matrixPower(n,A,b//2)
    if b%2:
        return matrixMultiple(n,A,matrixMultiple(n,r,r))
    return matrixMultiple(n,r,r)

n,b = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
for i in matrixPower(n,d,b):
    for j in i:
        print(j%1000,end=' ')
    print()