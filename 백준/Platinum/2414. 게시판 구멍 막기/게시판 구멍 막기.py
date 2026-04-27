n,m = map(int,input().split())
board = [list(input()) for i in range(n)]
hr = [[0]*m for i in range(n)]
vt = [[0]*m for i in range(n)]

cur = 0
bef = "*"
for i in range(n):
    if bef == "*":
        cur += 1
        bef = ""
    for j in range(m):
        if board[i][j] == "*":
            hr[i][j] = cur
        elif bef == "*":
            cur += 1
        bef = board[i][j]

cur2 = 0
bef2 = "*"
for j in range(m):
    if bef2 == "*":
        cur2 += 1
        bef2 = ""
    for i in range(n):
        if board[i][j] == "*":
            vt[i][j] = cur2
        elif bef2 == "*":
            cur2 += 1
        bef2 = board[i][j]
d = [[] for i in range(cur+1)]
for i in range(n):
    for j in range(m):
        if hr[i][j]:
            d[hr[i][j]].append(vt[i][j])

connected = [0]*(cur2+1)
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True

    for nx in d[x]:
        if not connected[nx] or dfs(connected[nx]):
            connected[nx] = x
            return True
    return False

ans = 0
for i in range(1,cur+1):
    visited = [False]*(cur+1)
    ans += dfs(i)
print(ans)
    