from collections import deque

n,k = map(int,input().split())
l = 200000

visited = [False]*l
distance = [0]*l

queue = deque([n])
while queue:
    x = queue.popleft()

    if x == k:
        break

    for i in (1,-1,x):
        if 0 <= (x + i) < l:

            if not visited[x+i]:
                visited[x+i] = True
                distance[x+i] = distance[x] + 1
                queue.append(x+i)

print(distance[k])