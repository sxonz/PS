from heapq import *

n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort(key=lambda x:(x[0],-x[1]))
ans = 0
curs,cure = -1,-1
h = 0
heap = []
for s,e in d:
    if s - 1 > cure:
        ans += (cure-curs+1)*h
        curs = s
        h = 1
    while heap and heap[0][0] < s:
        heappop(heap)
    cure = max(cure,e)
    heappush(heap,(e,s))
    h = max(h,len(heap))

print(ans+(cure-curs+1)*h)