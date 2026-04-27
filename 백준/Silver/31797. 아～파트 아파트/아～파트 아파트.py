from heapq import *
I = lambda:map(int,input().split())
n,m = I()
d = []
l = 0
for i in range(m):
    a,b = I()
    l = max(l,a,b)
    heappush(d,(a,i+1))
    heappush(d,(b,i+1))
for i in range(n):
    tmp,x = heappop(d)
    heappush(d,(l+1,x))
    l += 1
print(x)