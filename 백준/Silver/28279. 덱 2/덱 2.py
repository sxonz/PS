import sys
input = sys.stdin.readline
from collections import deque

queue = deque([])
l = 0
for i in range(int(input())):
    q,*r = map(int,input().split())
    if q == 1:
        queue.append(r[0])
        l += 1
    elif q == 2:
        queue.appendleft(r[0])
        l += 1
    elif q == 3:
        if l:
            print(queue.pop())
            l -= 1
        else:
            print(-1)
    elif q == 4:
        if l:
            print(queue.popleft())
            l -= 1
        else:
            print(-1)
    elif q == 5:
        print(l)
    elif q == 6:
        print(min(1,l)^1)
    elif q == 7:
        if l:
            print(queue[-1])
        else:
            print(-1)
    else:
        if l:
            print(queue[0])
        else:
            print(-1)
    