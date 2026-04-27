import sys
input = sys.stdin.readline
log = 20
m = int(input())
d = [0] + list(map(int,input().split()))
sparse = [[0]*log for _ in range(m+1)]

for i in range(1,m+1):
    sparse[i][0] = d[i]

for k in range(1,log):
    for i in range(1,m+1):
        sparse[i][k] = sparse[sparse[i][k-1]][k-1]

q = int(input())
for query in range(q):
    n,x = map(int,input().split())
    for k in range(log-1,-1,-1):
        if n >= 1<<k:
            x = sparse[x][k]
            n -= 1<<k
    print(x)