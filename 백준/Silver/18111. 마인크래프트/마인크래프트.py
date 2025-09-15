from heapq import *
n,m,b = map(int,input().split())

d = []
for i in range(n):
    d += list(map(int,input().split()))

d.sort(reverse=True)

_min = int(1e9)
idx = 0
for i in range(d[0]+1):
    B = b
    r = 0
    for j in d:
        if i-j < 0:
            r += -(i-j)*2
        else:
            r += i-j
        B -= i-j
        if B<0:
            break
    else:
        if _min >= r:
            _min = r
            idx = i
print(_min,idx)