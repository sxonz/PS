from collections import deque
n = int(input())
d = [input() for _ in range(n)]
edges = []
cost = 0
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j] == "0":
            continue
        if ord(d[i][j]) >= 97:
            graph[i].append(j)
            graph[j].append(i)
            cost += ord(d[i][j])-96
            edges.append((ord(d[i][j])-96,i,j))
            continue
        graph[i].append(j)
        graph[j].append(i)
        cost += ord(d[i][j])-38
        edges.append((ord(d[i][j])-38,i,j))
visit = [False]*n
visit[0] = True
queue = deque([0])
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if not visit[nx]:
            visit[nx] = True
            queue.append(nx)
flag = False in visit

edges.sort()
p = list(range(n+1))

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
def find(x):
    if x == p[x]:return x
    p[x] = find(p[x])
    return p[x]
def cycle(a,b):
    return find(a) == find(b)

for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        cost -= c
if flag:
    print(-1)
else:
    print(cost)