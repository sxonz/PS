from heapq import *
n,t,k = map(int,input().split())

heap = []
ans = 0
for i in range(n):
    query,*q = map(int,input().split())
    if query == 1:
        heappush(heap,(-q[1],q[0]))
    else:
        tmp = []
        for j in range(k):
            if not heap:
                break

            flag = False
            ncos,ntim = 0,0
            while heap:
                ncos,ntim = heappop(heap)
                if ntim < q[0]-t:
                    continue
                flag = True
                break
            if not flag:
                break
            ans -= ncos
print(ans)