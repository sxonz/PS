from collections import deque
dx = (-1,1,0,0)
dy = (0,0,-1,1)
def solution(land):
    m,n = len(land),len(land[0])
    oil = [-1]
    queue = deque()
    visited = [[False]*n for _ in range(m)]
    board = [[-1]*n for _ in range(m)]
    g = 0
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                queue.append((i,j))
                visited[i][j] = True
                g += 1
                board[i][j] = g
                o = 0
                while queue:
                    x,y = queue.popleft()
                    o += 1
                    for d in range(4):
                        nx,ny = dx[d]+x,dy[d]+y
                        if 0<=nx<m and 0<=ny<n:
                            if not visited[nx][ny] and land[nx][ny] == 1:
                                visited[nx][ny] = True
                                queue.append((nx,ny))
                                board[nx][ny] = g
                oil.append(o)
    answer = []
    for j in range(n):
        v = [False]*(len(oil)+1)
        temp = 0
        for i in range(m):
            if land[i][j] == 1:
                if not v[board[i][j]]:
                    v[board[i][j]] = True
                    temp += oil[board[i][j]]
        answer.append(temp)
    return max(answer)
            
                            