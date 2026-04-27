import sys
I = sys.stdin.readline
log = 18

n,m = map(int,I().split())
d = [int(I()) for _ in range(n)]
sparse = [[0]*log for i in range(n)]
for i in range(n):
    sparse[i][0] = d[i]
for k in range(1,log):
    for i in range(n):
        if i + (1<<k) - 1 >= n:
            break
        sparse[i][k] = min(sparse[i][k-1],sparse[i+(1<<(k-1))][k-1])
def size(l):
    for i in range(log):
        if 1<<i > l:
            return i-1
for i in range(m):
    a,b = map(int,I().split())
    l = size(b-a+1)
    print(min(sparse[a-1][l],sparse[b-(1<<l)][l]))
