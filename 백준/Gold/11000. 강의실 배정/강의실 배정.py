from heapq import *
n = int(input())
d = [tuple(map(int,input().split())) for _ in range(n)]
d.sort()

room = [d[0][1]]
size = 1
for s,e in d[1:]:
    l = heappop(room)
    if l>s:
        size += 1
        heappush(room,l)
    heappush(room,e)
print(size)
