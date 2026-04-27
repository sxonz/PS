from heapq import *
n = int(input())
r = [[] for _ in range(10001)]
for _ in range(n):
    a,b = map(int,input().split())
    r[b] += [a]
queue = []
ans = 0
for i in range(10000,0,-1):
    for j in r[i]:
        heappush(queue,-j)
    if queue:
        ans -= heappop(queue)
print(ans)