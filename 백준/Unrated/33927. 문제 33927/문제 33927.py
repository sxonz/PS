from collections import deque
dx = (-1,1,2,2,1,-1,-2,-2)
dy = (-2,-2,-1,1,2,2,1,-1)
n = int(input())
d = [list(map(int,input().split()))for i in range(n)]

queue = deque([])
for i in range(n):
    for j in range(n):
        queue.append((d[i][j],[(i,j)]))
visited = []
m = 0
while queue:
    cur,board = queue.popleft()
    m = max(cur,m)
    for i in range(n):
        for j in range(n):
            if (i,j) in board:continue
            flag = 1
            for k in range(8):
                nx,ny = i+dx[k],j+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if (nx,ny) in board:
                        flag = 0
                        break
            if flag:
                tmp = board+[(i,j)]
                tmp.sort()
                if tmp not in visited:
                    queue.append((cur+d[i][j],tmp)) 
                    visited.append(tmp)
print(m)

