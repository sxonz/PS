import sys
input = sys.stdin.readline
from collections import deque

queue = deque([])
l = 0
for i in range(int(input())):
    q,*r = input().split()
    if q == "push":
        queue.append(int(r[0]))
        l += 1
    elif q == "pop":
        if l:
            print(queue.popleft())
            l -= 1
        else:
            print(-1)
    elif q == "size":
        print(l)
    elif q == "empty":
        print(min(1,l)^1)
    elif q == "front":
        if l:
            print(queue[0])
        else:
            print(-1)
    else:
        if l:
            print(queue[-1])
        else:
            print(-1)