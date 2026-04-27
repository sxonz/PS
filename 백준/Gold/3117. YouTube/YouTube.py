log = 42

n,k,m = map(int,input().split())
query = list(map(int,input().split()))
d = list(map(int,input().split()))

sparse = [[0]*log for _ in range(k+1)]

for i in range(1,k+1):
    sparse[i][0] = d[i-1]

for l in range(1,log):
    for i in range(1,k+1):
        sparse[i][l] = sparse[sparse[i][l-1]][l-1]

m -= 1
for l in range(log-1,-1,-1):
    if m >= 1<<l:
        for q in range(n):
            query[q] = sparse[query[q]][l]
        m -= 1<<l

print(*query)