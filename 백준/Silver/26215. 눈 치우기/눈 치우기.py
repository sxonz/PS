from heapq import *
n = int(input())
d = list(map(int,input().split()))
d = [-i for i in d]
heapify(d)
r = 0
while len(d) > 1:
    a = -heappop(d)
    b = -heappop(d)
    m = min(a,b)
    a -= m
    b -= m
    r += m
    if a:
        heappush(d,-a)
    if b:
        heappush(d,-b)
if d:
    r += -d[0]
print((r+1) * (r <= 1440) - 1)