import sys
input = sys.stdin.readline

from heapq import *

n = int(input())
arr = []

for i in range(n):
    order = int(input())
    if order == 0:
        if arr:
            print(heappop(arr))
        else:
            print(0)
    else:
        heappush(arr,order)