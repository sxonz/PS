dx = (-2,-2,-1,1,2,2,1,-1)
dy = (-1,1,2,2,1,-1,-2,-2)
n = int(input())
x,y = map(int,input().split())
cx,cy = x-1,y-1
r = [(cx,cy)]
visited = [[0]*n for i in range(n)]
visited[cx][cy] = 1
def check(x,y):
    res = 0
    for i in range(8):
        nx,ny = cx+dx[i],cy+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                res += 1
    return res
for c in range(n*n-1):
    tmp = []
    for i in range(8):
        nx,ny = cx+dx[i],cy+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                tmp.append((check(nx,ny),nx,ny))
    if not tmp:
        break
    cx,cy = min(tmp)[1:]
    visited[cx][cy] = 1
    r.append((cx,cy))

if len(r) == n*n:
    for i in r:
        print(*i)
else:
    print(-1,-1)
