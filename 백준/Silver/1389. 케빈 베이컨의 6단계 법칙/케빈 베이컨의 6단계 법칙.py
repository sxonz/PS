from collections import deque
n,m = map(int,input().split())
d = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

bacon = [0] * (n+1)
for people in range(1,n+1):
    queue = deque([people])
    visited = [False] * (n+1)
    distance = [0] * (n+1)

    while queue:
        x = queue.popleft()
        visited[x] = True

        for i in d[x]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[x] + 1
                queue.append(i)
    bacon[people] = sum(distance)
bacon[0] = 2**31

min_ = min(bacon)

for i in range(1,n+1):
    if bacon[i] == min_:
        print(i)
        break



