from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs():
    c = 0
    while queue:
        x,y = queue.popleft()
        c += 1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny] and d[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return c


m,n,k = map(int,input().split())
d = [[0]*n for _ in range(m)]



for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            d[y][x] = 1

queue = deque()
visited = [[False]*n for _ in range(m)]
answer = []

cnt = 0
for i in range(m):
    for j in range(n):
        if d[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            queue.append((i,j))
            cnt += 1
            answer.append(bfs())
print(cnt)
print(*sorted(answer))