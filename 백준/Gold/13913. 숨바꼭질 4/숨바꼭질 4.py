from collections import deque

n,k = map(int,input().split())
l = 200000

visited = [False]*l
distance = [0]*l
d = [0]*l

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
                d[x+i] = x
                queue.append(x+i)

result = []
temp = [n]
for _ in range(distance[k]):
    result.append(x)
    x = d[x]
temp.extend(reversed(result))
print(distance[k])
print(*temp)