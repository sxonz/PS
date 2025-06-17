from heapq import heappush, heappop

n,k = map(int,input().split())
d = [0] + list(map(int,input().split()))

heap = []
for i in range(1,k+1):
    heappush(heap,(-d[i],i))

res = []
bef = -1
while heap:
    r,c = heappop(heap)
    if c == bef:
        if not heap:
            print(-1)
            break
        r2,c2 = heappop(heap)
        heappush(heap,(r,c))
        r,c = r2,c2
    res.append(c)
    if r+1:
        heappush(heap, (r+1,c))
    bef = c
else:
    print(*res)

