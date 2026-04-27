from collections import deque
t = int(input())

dx = (-2,-2,-1,1,2,2,1,-1)
dy = (-1,1,2,2,1,-1,-2,-2)

for test in range(t):
    n = int(input())
    chess = [[0]*n for _ in range(n)]
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())

    queue = deque([(sx,sy)])
    visited = [[False]*n for _ in range(n)]

    while queue:
        x,y = queue.popleft()
        if x == ex and y == ey:
            print(chess[ex][ey])
            break
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    chess[nx][ny] = chess[x][y] + 1
                    queue.append((nx,ny))