from collections import deque

dx = (-1,1,-1,1,-1,1,0,0)
dy = (-1,-1,0,0,1,1,-1,1)

def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<h and 0<=ny<w:
                if d[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    
answer = []

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    d = [input().split() for _ in range(h)]

    cnt = 0
    visited = [[False]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and d[i][j] == '1':
                visited[i][j] = True
                bfs(i,j)
                cnt += 1
    answer.append(cnt)

print(*answer,sep='\n')