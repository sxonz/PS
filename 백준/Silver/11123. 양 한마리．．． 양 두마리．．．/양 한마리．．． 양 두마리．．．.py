from collections import deque
dx = (-1,1,0,0)
dy = (0,0,-1,1)

testcase = int(input())
ans = []
for _ in range(testcase):
    n,m = map(int,input().split())
    d = []
    for i in range(n):
        d.append(input())
    visited = [[False]*m for i in range(n)]
    queue = deque([])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and d[i][j] == "#":
                queue.append((i,j))
                cnt += 1
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<m:
                            if not visited[nx][ny] and d[nx][ny] == "#":
                                visited[nx][ny] = True
                                queue.append((nx,ny))
    ans.append(cnt)
for i in ans:
    print(i)
