from heapq import *

n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()
heap = []
ans = 0
cur = 0
for s,e in d:
    while heap and heap[0][0] <= s:
        heappop(heap)
        cur -= 1
    heappush(heap,(e,s))
    cur += 1
    ans = max(ans,cur)
print(ans)