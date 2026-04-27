from heapq import *

n = int(input())
d = []
m = 0
for i in range(n):
    a,b = map(int,input().split())
    d.append((a,b))
    m = max(m,a)
queue = []
ans = 0
for i in range(m,0,-1):
    for j in d:
        if j[0] == i:
            heappush(queue,-j[1])
    if queue:
        ans -= heappop(queue)
print(ans)
