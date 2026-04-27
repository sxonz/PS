from heapq import *

n,k = map(int,input().split())
d = sorted(list(map(int,input().split())))
d.insert(0,0)
tmp = []
for i in range(1,n+1):
    tmp.append(d[i]-d[i-1])
heapify(tmp)

cnt = n-k
ans = 0
for i in range(cnt):
    ans += heappop(tmp)

print(ans)