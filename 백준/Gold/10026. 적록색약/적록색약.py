from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(color):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and d[nx][ny] in color:
                    visited[nx][ny]= True
                    queue.append((nx,ny))


n = int(input())
d = [input() for _ in range(n)]

queue = deque()
visited = [[False]*n for _ in range(n)]
cnt1,cnt2 = 0,0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            queue.append((i,j))
            cnt1 += 1
            bfs(d[i][j])
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            queue.append((i,j))
            cnt2 += 1
            if d[i][j] in 'RG':
                bfs('RG')
            else:
                bfs('B')
print(cnt1)
print(cnt2)