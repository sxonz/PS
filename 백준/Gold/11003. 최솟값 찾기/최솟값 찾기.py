from collections import deque

n,l = map(int,input().split())
d = list(map(int,input().split()))

queue = deque([])
res = []

for i in range(n):
    while queue and queue[-1][0] >= d[i]:
        queue.pop()
    queue.append((d[i],i))
    if queue[0][1] <= i-l:
        queue.popleft()
    res.append(queue[0][0])
print(*res)