from collections import deque

r = [2**i for i in range(11)]
s,e = int(input(),2),int(input(),2)
m = 1 << 11
distance = [0]*5000
visited = [False]*5000
visited[s] = True
queue = deque([s])
while queue:
    x = queue.popleft()
    if x:
        if not visited[x-1]:
            visited[x-1] = True
            distance[x-1] = distance[x] + 1
            queue.append(x-1)
    if x <= 1024:
        if not visited[x+1]:
            visited[x+1] = True
            distance[x+1] = distance[x] + 1
            queue.append(x+1)
    top = 0
    for i in range(10):
        if x < r[i+1]:
            break
        if not visited[x ^ r[i]]:
            visited[x ^ r[i]] = True
            queue.append(x ^ r[i])
            distance[x ^ r[i]] = distance[x] + 1
print(distance[e])