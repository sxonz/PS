from collections import deque

n,m = map(int,input().split())
tomato = [list(input().split()) for _ in range(m)]

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def check(arr):
    for i in arr:
        for j in i:
            if j == '0':
                return True
    return False

queue = deque([])
visited = [[False]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if tomato[i][j] == '1':
            queue.append((i,j))

if check(tomato):
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny] and tomato[nx][ny] == '0':
                    visited[nx][ny] = True
                    tomato[nx][ny] = str(int(tomato[x][y]) + 1)
                    queue.append((nx,ny))

    if check(tomato):
        print(-1)
    else:
        day = 0
        for t in tomato:
            for t2 in t:
                if int(t2) > day:
                    day = int(t2)
        print(day-1)

else:
    print(0)