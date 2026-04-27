import sys
sys.setrecursionlimit(200001)
I = lambda:map(int,sys.stdin.readline().split())
n = int(input())
color = list(I())
color = [0] + color
d = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = I()
    d[a].append(b)
    d[b].append(a)

c = [0]*(n+1)
cnt = 0
visited = [False]*(n+1)
visited[1] = True
def dfs(x,cur):
    global cnt
    if cur != color[x]:
        cur = color[x]
        cnt += 1
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx,cur)
dfs(1,0)
print(cnt)