from heapq import *
n = int(input())
d = list(map(int,input().split()))
d.sort()
r = 0
for i in d:
    if i-1 > r:
        print(r+1)
        break
    r += i
else:
    print(r+1)