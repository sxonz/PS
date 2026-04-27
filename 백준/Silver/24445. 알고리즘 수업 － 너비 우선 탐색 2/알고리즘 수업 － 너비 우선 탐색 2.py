from collections import deque

n,m,r = map(int,input().split())
d = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

for i in d:
    i.sort(reverse=True)

queue = deque([r])
visited = [False]*(n+1)
visited[r] = True
distance = [0] * (n+1)
distance[r] = 1
temp = 2

while queue:
    x = queue.popleft()

    for i in d[x]:
        if not visited[i]:
            visited[i] = True
            distance[i] = temp
            temp += 1
            queue.append(i)

for i in distance[1:]:
    print(i)