from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(h):
     while queue:
          x,y = queue.popleft()

          for i in range(4):
               nx,ny = x + dx[i], y + dy[i]
               if 0<=nx<n and 0<=ny<n:
                    if not visited[nx][ny] and int(d[nx][ny]) > h:
                         visited[nx][ny] = True
                         queue.append((nx,ny))

          
n = int(input())
d = [input().split() for _ in range(n)]

queue = deque()
visited = [[False]*n for _ in range(n)]

m = 0
for i in d:
    m = max(m,max(map(int,i)))

cnt = [0] * m
for i in range(m):
    visited = [[False]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if int(d[j][k]) > i and not visited[j][k]:
                   visited[j][k] = True
                   queue.append((j,k))
                   bfs(i)
                   cnt[i] += 1
print(max(cnt))