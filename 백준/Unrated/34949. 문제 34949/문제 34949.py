from collections import deque

n = int(input())
d = list(map(int,input().split()))
d = [i-1 for i in d]

graph = [[] for i in range(n)]
for i in range(n):
    graph[d[i]].append(i)

queue = deque([n-1])
distance = [-1]*n
distance[-1] = 0
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if distance[nx] == -1:
            distance[nx] = distance[x] + 1
            queue.append(nx)
print(*distance,sep='\n')
