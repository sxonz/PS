n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

dx = (0,1,1)
dy = (1,1,0)
check = [[(0,1)], ((0,1),(1,1),(1,0)), [(1,0)]]
dp = [[[0,0,0] for i in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(1,n):
        for dir in range(3):
            if not dp[i][j][dir]:
                continue
            for ndir in range(max(0,dir-1), min(2,dir+1)+1):
                flag = 0
                for ci,cj in check[ndir]:
                    cx = i+ci
                    cy = j+cj
                    if 0<=cx<n and 0<=cy<n:
                        flag |= d[cx][cy]
                    else:
                        flag = 1
                        break
                if flag:
                    continue
                nx = i + dx[ndir]
                ny = j + dy[ndir]
                dp[nx][ny][ndir] += dp[i][j][dir]

print(sum(dp[n-1][n-1]))