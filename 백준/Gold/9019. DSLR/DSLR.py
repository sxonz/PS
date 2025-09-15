from collections import deque
import sys
input = sys.stdin.readline
M = 10000

for t in range(int(input())):
    a,b = map(int,input().split())
    visited = [0]*M
    queue = deque([(a,'')])
    while queue:
        x,o = queue.popleft()
        if x == b:
            print(o)
            break

        nx = x*2%M
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx,o+"D"))
        nx = (x-1)%M
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx,o+"S"))
        nx = x%1000*10+x//1000
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx,o+"L"))
        nx = x//10+x%10*1000
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx,o+"R"))