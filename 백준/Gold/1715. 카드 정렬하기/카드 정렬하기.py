from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]
heapify(d)
res = 0

while len(d) >= 2:
    a = heappop(d)
    b = heappop(d)
    heappush(d,a+b)
    res += a+b
print(res)