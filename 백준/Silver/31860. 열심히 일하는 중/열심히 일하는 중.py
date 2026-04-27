from heapq import *
import math

n,m,k = map(int,input().split())
queue = [-int(input()) for _ in range(n)]
heapify(queue)

happy = 0
day = 0
h = []
while queue:
    day += 1
    x = heappop(queue)
    happy = math.floor(happy/2) - x
    x += m
    if x < -k:
        heappush(queue,x)
    h.append(happy)
print(day)
for i in h:
    print(i)