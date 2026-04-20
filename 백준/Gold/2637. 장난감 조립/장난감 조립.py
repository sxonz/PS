from collections import deque

n,m = int(input()),int(input())
base = [True]*(n+1)
base[0] = False
indegree = [0]*(n+1)
indegree[0] = -1
d = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    indegree[b] += 1
    d[a].append((b,c))
    base[a] = False

price = [0 for _ in range(n+1)]
price[n] = 1
queue = deque([n])
while queue:
    x = queue.popleft()
    for nx,cost in d[x]:
        indegree[nx] -= 1
        price[nx] += price[x]*cost
        if indegree[nx] == 0:
            queue.append(nx)

for i in range(n+1):
    if base[i]:
        print('{0} {1}'.format(i,price[i]))