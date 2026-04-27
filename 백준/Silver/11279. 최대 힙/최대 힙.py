import sys
input = sys.stdin.readline

from heapq import *

n = int(input())
arr = []
heapify(arr)

for i in range(n):
    o = int(input())
    if o == 0:
        if arr:
            print(0-heappop(arr))
        else:
            print(0)
    heappush(arr,0-o)