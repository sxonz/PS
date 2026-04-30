from collections import deque
dx = (-1,1,0,0)
dy = (0,0,-1,1)
def solution(maps):
    n,m = len(maps),len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = (i,j)
            elif maps[i][j] == 'E':
                e = (i,j)
            elif maps[i][j] == 'L':
                l = (i,j)
    queue = deque([s])
    visited = [[False]*m for _ in range(n)]
    visited[s[0]][s[1]] = True
    distance = [[0]*m for _ in range(n)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    distance[nx][ny] = distance[x][y] + 1
    if not visited[l[0]][l[1]]:return -1
    td = distance[l[0]][l[1]]
    queue = deque([l])
    visited = [[False]*m for _ in range(n)]
    visited[l[0]][l[1]] = True
    distance = [[0]*m for _ in range(n)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    distance[nx][ny] = distance[x][y] + 1
    if not visited[e[0]][e[1]]:return -1
    return td + distance[e[0]][e[1]]