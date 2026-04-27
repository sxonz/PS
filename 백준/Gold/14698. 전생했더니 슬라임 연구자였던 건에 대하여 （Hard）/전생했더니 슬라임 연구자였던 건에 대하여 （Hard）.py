import sys
input = sys.stdin.readline
from heapq import *
MOD = 1000000007
for test in range(int(input())):
    n = int(input())
    heap = list(map(int,input().split()))
    ans = 1

    heapify(heap)
    while len(heap) >= 2:
        a,b = heappop(heap),heappop(heap)
        ans *= a*b%MOD
        heappush(heap,a*b)
    print(ans%MOD if ans else 1)