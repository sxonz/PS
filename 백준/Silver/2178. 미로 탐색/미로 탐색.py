from collections import deque
n,m = map(int,input().split())
maze = [list(input()) for _ in range(n)]

for load in maze:
    load = list(map(int,load))

dx = (-1,1,0,0)
dy = (0,0,-1,1)

queue = deque([(0,0)])
visited = [[False]*m for _ in range(n)]

while queue:
    x,y = queue.popleft()

    for i in range(4):

        nx,ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and maze[nx][ny] != '0':
                visited[nx][ny] = True
                maze[nx][ny] = str(int(maze[x][y]) + 1)
                queue.append((nx,ny))
print(maze[n-1][m-1])