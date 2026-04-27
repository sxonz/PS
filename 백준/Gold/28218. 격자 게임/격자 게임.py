def int_(a):
    return int(a)-1

n,m,k = map(int,input().split())
case = k+2
dx = [1,0]
for i in range(k):
    dx.append(i+1)
dy = [0,1]
for i in range(k):
    dy.append(i+1)

board = []
for i in range(n):
    board.append(list(input()))
query = []
q = int(input())
for i in range(q):
    query.append(tuple(map(int_,input().split())))

dp = [[False]*(m) for _ in range(n)]
for i in reversed(range(n)):
    for j in reversed(range(m)):
        for dir in range(case):
            ni,nj = i+dx[dir],j+dy[dir]
            if 0<=ni<n and 0<=nj<m and board[ni][nj] == '.':
                if not dp[ni][nj]:
                    dp[i][j] = True
res = []
for pos in query:
    x,y = pos
    ans = 'First' if dp[x][y] else 'Second'
    res.append(ans)
            
for i in res:
    print(i)