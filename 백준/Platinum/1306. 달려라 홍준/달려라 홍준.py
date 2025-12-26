from collections import deque

n,k = map(int,input().split())
d = list(map(int,input().split()))

queue = deque([])

ans = []
for i in range(n):
    if queue and queue[0][0] <= i-2*k+1:
        queue.popleft()
    while queue and queue[-1][1] < d[i]:
        queue.pop()
    queue.append((i,d[i]))
    if i >= 2*k-2:
        ans.append(queue[0][1])
print(*ans)