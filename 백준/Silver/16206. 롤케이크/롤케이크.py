from heapq import *
n,m = map(int,input().split())
d = list(map(int,input().split()))
heap = [(i if i%10==0 and i>=20 else int(1e9),-i) for i in d]
heapify(heap)
for i in range(m):
    tmp,x = heappop(heap)
    if -x <= 10:
        heappush(heap,(tmp,x))
        break
    heappush(heap,(-x-10 if -x >= 30 else int(1e9),x+10))
    heappush(heap,(int(1e9),-10))
ans = sum([1 for i in heap if i[1] == -10])
print(ans)