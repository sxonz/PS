from heapq import *
from collections import deque

n,k = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
c = sorted([int(input()) for _ in range(k)])
d.sort(key=lambda x:(x[0],-x[1]))
d = deque(d)
tmp = []
heapify(tmp)
ans = 0
for i in range(k):
    while d and d[0][0] <= c[i]:
        heappush(tmp,-d[0][1])
        d.popleft()
    if not tmp:
        continue
    choice = heappop(tmp)
    ans += choice
print(-ans)