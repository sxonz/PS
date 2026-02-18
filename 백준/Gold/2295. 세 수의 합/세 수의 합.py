import sys
from bisect import *
input = sys.stdin.readline
n = int(input())
d = [int(input()) for i in range(n)]
d.sort()
val = []
ans = 0

for i in range(n):
    for j in range(i,n):
        insort_right(val,d[i]+d[j])
    for k in range(i,n):
        idx = bisect_right(val,d[k]-d[i])
        if idx:
            if val[idx-1] == d[k]-d[i]:
                ans = max(ans,d[k])

print(ans)