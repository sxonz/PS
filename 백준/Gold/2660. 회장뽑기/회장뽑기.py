from collections import deque

n = int(input())
d = [[] for _ in range(n+1)]
while True:
    a,b = map(int,input().split())
    if a+b == -2:
        break
    d[a].append(b)
    d[b].append(a)

people = [0]*(n+1)
people[0] = 314159265358979


for i in range(1,n+1):
    queue  = deque([])
    queue.append(i)

    visited = [False]*(n+1)
    visited[i] = True

    distance = [0]*(n+1)
    while queue:
        x = queue.popleft()

        for nx in d[x]:
            if not visited[nx]:
                visited[nx] = True
                distance[nx] = distance[x] + 1
                queue.append(nx)
    people[i] = max(distance)

_m = min(people)
print(_m,people.count(_m))
for i in range(n+1):
    if people[i] == _m:
        print(i,end=' ')