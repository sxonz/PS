from heapq import *
n,m = map(int,input().split())
heap = list(map(int,input().split()))
heapify(heap)
for i in range(m):
    a,b = heappop(heap),heappop(heap)
    heappush(heap,a+b)
    heappush(heap,a+b)
print(sum(heap))