import sys
from collections import deque
input = sys.stdin.readline
dx = (-1,1,0,0)
dy = (0,0,-1,1)
while True:
    n,m,k = map(int,input().split())
    if [n,m,k] == [0,0,0]:
        break
    d = []
    for i in range(n):
        tmp = []
        for j in range(m):
            t = input().rstrip('\n')
            if 'S' in t:
                start = (i,j,t.index('S'))
            if 'E' in t:
                end = (i,j,t.index('E'))
            tmp.append(t)
        input()
        d.append(tmp)

    queue = deque([])
    queue.append((start,0))
    visited = [[[False]*k for g in range(m)] for h in range(n)]
    visited[start[0]][start[1]][start[2]] = True
    flag = False
    while queue:
        pos,depth = queue.popleft()
        floor,x,y = pos
        if d[floor][x][y] == 'E':
            break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<k:
                if not visited[floor][nx][ny] and d[floor][nx][ny] != '#':
                    visited[floor][nx][ny] = True
                    queue.append(((floor,nx,ny),depth+1))
        if floor+1 <n:
            if not visited[floor+1][x][y] and d[floor+1][x][y] != '#':
                visited[floor+1][x][y] = True
                queue.append(((floor+1,x,y),depth+1))
        if floor-1 >=0:
            if not visited[floor-1][x][y] and d[floor-1][x][y] != '#':
                visited[floor-1][x][y] = True
                queue.append(((floor-1,x,y),depth+1))
    else:
        flag = True
    if flag or depth == 0:
        print('Trapped!')
    else:
        print('Escaped in {0} minute(s).'.format(depth))