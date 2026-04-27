import sys
input = sys.stdin.readline
from heapq import *
day = 0
while True:
    day += 1
    n = int(input())
    idx = 0
    if not n:
        break
    d = [tuple(map(int,input().split())) for i in range(n)]
    d.sort()
    heap = []
    ans = 0
    for i in range(8,25):
        while idx < n:
            if d[idx][0] == i:
                heappush(heap,d[idx][1])
                idx += 1
            else:
                break
        cnt = 0
        while heap and cnt < 2:
            tmp = heappop(heap)
            if tmp > i:
                cnt += 1
                ans += 1
    print(f"On day {day} Emma can attend as many as {ans} parties.")
    