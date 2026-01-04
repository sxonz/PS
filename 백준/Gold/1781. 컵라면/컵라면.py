from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
d = [[] for i in range(n+1)]
for i in range(n):
    a,b = map(int,input().split())
    d[a].append(b)

heap = []
ans = 0
for i in range(n,0,-1):
    for j in d[i]:
        heappush(heap,-j)
    if heap:
        ans -= heappop(heap)
print(ans)