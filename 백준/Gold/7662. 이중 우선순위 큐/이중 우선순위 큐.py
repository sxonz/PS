import sys
from collections import defaultdict
from heapq import *
for test in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    minheap = []
    maxheap = []
    key = defaultdict(int)
    for i in range(n):
        query,q = sys.stdin.readline().split()
        if query == "I":
            heappush(minheap,int(q))
            heappush(maxheap,-int(q))
            key[int(q)] += 1
        else:
            if q == "1":
                while maxheap:
                    x = -heappop(maxheap)
                    if key[x]:
                        key[x] -= 1
                        break
            else:
                while minheap:
                    x = heappop(minheap)
                    if key[x]:
                        key[x] -= 1
                        break
    ans1 = None
    while maxheap:
        tmp = -heappop(maxheap)
        if key[tmp]:
            ans1 = tmp
            break

    while minheap:
        ans2 = heappop(minheap)
        if key[ans2]:
            break
    
    if ans1 is None:
        print("EMPTY")
    else:
        print(ans1,ans2)