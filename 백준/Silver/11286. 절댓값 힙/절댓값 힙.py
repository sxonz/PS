import sys
input = sys.stdin.readline

from heapq import *

arr = []
n = int(input())

for i in range(n):
    order = int(input())
    if order == 0:
        if arr:
            print(heappop(arr)[1])
        else:
            print(0)
    else:
        heappush(arr,(abs(order),order))