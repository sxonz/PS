from collections import deque

n = int(input())

d = [[] for _ in range(n+1)]
time = [0]*(n+1)
indegree = [0]*(n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    time[i] = tmp[0]

    for j in tmp[1:-1]:
        indegree[i] += 1
        d[j].append(i)

queue = deque([])
for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

price = [0]*(n+1)
while queue:
    x = queue.popleft()

    for nx in d[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            queue.append(nx)
        price[nx] = max(price[nx],price[x]+time[x])
for i in range(1,n+1):
    print(price[i]+time[i])
        