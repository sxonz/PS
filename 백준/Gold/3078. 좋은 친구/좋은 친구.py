from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())
queue = deque([])

res = 0

l = [0 for _ in range(25)]
for i in range(n):
    name = input()
    queue.append(name)
    if len(queue) > k+1:
        l[len(queue.popleft())] -= 1
    res += l[len(name)]
    l[len(name)]+=1
print(res)