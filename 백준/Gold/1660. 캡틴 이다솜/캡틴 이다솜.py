from collections import deque
n = int(input())
prefix_sum = [0]
for i in [i*(i+1) // 2 for i in range(1,121)]:
    prefix_sum.append(prefix_sum[-1]+i)
queue = deque([0])
M = 300000
visited = [False]*(M+1)
visited[0] = True
cannonball = [0]*(M+1)
while queue:
    x = queue.popleft()
    for nx in prefix_sum:
        if x+nx > M:
            continue
        if not visited[x+nx]:
            visited[x+nx] = True
            queue.append(x+nx)
            cannonball[x+nx] = cannonball[x]+1
print(cannonball[n])