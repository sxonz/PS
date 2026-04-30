from heapq import *
def solution(n, works):
    works = [-w for w in works]
    heapify(works)
    for i in range(n):
        tmp = heappop(works)
        if tmp == 0:
            break
        heappush(works,tmp+1)
    return sum([i**2 for i in works])