n,m = map(int,input().split())
d = list(map(int,input().split()))
board = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(d[i]):
        board[i][j] = 1
cnt = 0
for i in range(m):
    for j in range(n):
        if not board[i][j]:
            flag = False
            for k in range(i):
                if board[k][j]:
                    break
            else:
                flag |= True
            for k in range(i+1,m):
                if board[k][j]:
                    break
            else:
                flag |= True
            cnt += flag^1
print(cnt)
