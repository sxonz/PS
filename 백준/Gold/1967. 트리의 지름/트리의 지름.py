from collections import deque

n = int(input())
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

def bfs(i):
    while queue:
        x,t = queue.popleft()
        for nx,nt in d[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append((nx,t+nt))
                distance[nx] = t+nt
    return distance.index(max(distance))

queue = deque()
temp = []
visited  = [False]*(n+1)
distance = [0]*(n+1)
visited[1] = True
queue.append((1,0))

temp = bfs(1)

visited = [False]*(n+1)
distance = [0]*(n+1)
visited[temp] = True
queue.append((temp,0))

print(distance[bfs(temp)])