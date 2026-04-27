from collections import deque

n = int(input())
d = [input() for _ in range(n)]

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(x,y):
    cnt = 0
    queue = deque([(x,y)])

    while queue:
        cnt += 1
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:

                if d[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))



    return cnt

visited = [[False]*n for _ in range(n)]
answer = []
tmp = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j] and d[i][j] == '1':  
            tmp += 1
            visited[i][j] = True
            answer.append(bfs(i,j))
            
print(tmp)
print(*sorted(answer),sep='\n')