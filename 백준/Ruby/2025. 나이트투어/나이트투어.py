dx = (-2,-2,-1,1,2,2,1,-1)
dy = (-1,1,2,2,1,-1,-2,-2)
n = int(input())
x,y = map(int,input().split())
for i in range(10):
    cx,cy = x-1,y-1
    r = [(cx+1,cy+1)]
    visited = [[0]*n for i in range(n)]
    visited[cx][cy] = 1
    def check(x,y):
        res = 0
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    res += 1
        return res
    def dist(x,y):
        return (n/2-x)**2+(n/2-y)**2
    for c in range(n*n-1):
        tmp = []
        for i in range(8):
            nx,ny = cx+dx[i],cy+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    tmp.append((check(nx,ny),dist(nx,ny),nx,ny))
        if not tmp:
            break
        cx,cy = min(tmp)[2:]
        visited[cx][cy] = 1
        r.append((cx+1,cy+1))

    if len(r) == n*n:
        for i in r:
            print(*i)
        exit()
print(-1,-1)
