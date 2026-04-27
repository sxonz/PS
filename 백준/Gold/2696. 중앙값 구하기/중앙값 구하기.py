from heapq import *

ans = []
for t in range(int(input())):
    n = int(input())
    ans.append([n//2+n%2])
    d = []
    for i in range(n//10+bool(n%10)):
        d += list(map(int,input().split()))
    minh = []
    minl = 0
    maxh = []
    maxl = 0
    tmp = []
    for idx,i in enumerate(d):
        heappush(minh,i)
        minl += 1
        if maxl and minl and -maxh[0] > minh[0]:
            heappush(minh,-heappop(maxh))
            heappush(maxh,-heappop(minh))
        if minl > maxl+1:
            heappush(maxh,-heappop(minh))
            minl -= 1
            maxl += 1
        if idx%2==0:
            tmp.append(minh[0])
    for i in range(len(tmp)//10):
        ans.append(tmp[i*10:i*10+10])
    if len(tmp)%10:
        ans.append(tmp[len(tmp)//10*10:])
for i in ans:
    print(*i)
