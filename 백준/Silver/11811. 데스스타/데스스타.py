n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
ans = [0]*n
for i in range(n):
    for j in range(n):
        ans[i] |= d[i][j]
        ans[j] |= d[i][j]
print(*ans)