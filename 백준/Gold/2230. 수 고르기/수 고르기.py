import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
d = [int(input()) for i in range(n)]
d.sort()

ans = int(1e12)
queue = deque([])
l = 0
for i in d:
    while l >= 2 and i >= queue[1]:
        queue.popleft()
        l -= 1
    queue.append(i+m)
    l += 1
    if queue[0] <= i:
        ans = min(ans,i-queue[0]+m)
print(ans)