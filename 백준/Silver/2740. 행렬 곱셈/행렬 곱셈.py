def multiple(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

n,m = map(int,input().split())
arr1 = [(list(map(int,input().split()))) for _ in range(n)]
m,k = map(int,input().split())
arr2 = [(list(map(int,input().split()))) for _ in range(m)]
d = multiple(arr1,arr2)
for i in d:
    print(' '.join([str(j) for j in i]))