from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
maxH = []
minH = []
res = []
for i in range(2,n+2):
    cur = int(input())
    if not minH or cur >= minH[0]:
        heappush(minH,cur)
    else:
        heappush(maxH,-cur)
        
    if len(maxH) < i//2:
        heappush(maxH,-heappop(minH))
    elif len(minH) < (i-1)//2:
        heappush(minH,-heappop(maxH))
    elif -maxH[0] > minH[0]:
        heappush(minH,-heappop(maxH))
        heappush(maxH,-heappop(minH))
    print(-maxH[0])
