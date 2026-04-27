from collections import deque

n,o,s,e = map(int,input().split())
d = [[[] for i in range(n+1)] for j in range(o+1)]
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    for j in range(1,o+1):
        d[j][a].append((j,b))
        d[j][b].append((j,a))
p = int(input())
for i in range(p):
    x,a = map(int,input().split())
    d[x][a].append((x+1,a))
    d[x+1][a].append((x,a))
queue = deque([(1,s)])
visited = [[False]*(n+1) for _ in range(o+1)]
visited[1][s] = True
distance = [[[0,0] for i in range(n+1)] for _ in range(o+1)]
while queue:
    sp,x = queue.popleft()
    for ns,nx in d[sp][x]:
        if not visited[ns][nx]:
            visited[ns][nx] = True
            distance[ns][nx] = distance[sp][x][::]
            if sp != ns:
                distance[ns][nx][1] += 1
            else:
                distance[ns][nx][0] += 1
            queue.append((ns,nx))
q = int(input())
for query in range(q):
    a,b = map(int,input().split())
    if not visited[o][e]:
        print(-1)
    else:
        r,w = distance[o][e]
        print(r*a+w*b)