import sys
input = sys.stdin.readline

n,m = map(int,input().split())
r = 21
d = [[0]*r for i in range(n+1)]
for _ in range(m):
    query,*q = map(int,input().split())
    if query == 1:
        d[q[0]][q[1]] = 1
    elif query == 2:
        d[q[0]][q[1]] = 0
    elif query == 3:
        for i in range(r-1,1,-1):
            d[q[0]][i] = d[q[0]][i-1]
        d[q[0]][1] = 0
    else:
        for i in range(r-1):
            d[q[0]][i] = d[q[0]][i+1]
        d[q[0]][-1] = 0

print(len(set([tuple(i[1:]) for i in d[1:]])))