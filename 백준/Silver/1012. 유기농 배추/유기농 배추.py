from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and d[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

t = int(input())
answer = []

for test in range(t):
    n,m,k = map(int,input().split())

    d = [[0]*m for _ in range(n)]

    for i in range(k):
        x,y = map(int,input().split())
        d[x][y] = 1

    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and d[i][j] == 1:
                visited[i][j] = True
                bfs(i,j)
                cnt += 1
    answer.append(cnt)
print(*answer,sep='\n')