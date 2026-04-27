def dfs(x):
    global cnt

    flag = False
    for nx in d[x]:
        if not visited[nx]:
            flag = True
            dfs(nx)

    if not flag:
        cnt += 1




n = int(input())
d = [[] for _ in range(n)]

temp = list(map(int,input().split()))

for i in range(n):
    if temp[i] != -1:
        d[temp[i]].append(i)

r = temp.index(-1)
cnt = 0
visited = [False]*(n+1)
visited[r] = True
delete = int(input())
if delete == r:
    print(0)
else:
    visited[delete] = True
    dfs(r)
    print(cnt)
