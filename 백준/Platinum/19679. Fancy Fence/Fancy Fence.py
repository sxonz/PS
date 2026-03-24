import sys
sys.setrecursionlimit(100000)
n = int(input())
d = [tuple(map(int,input().split())) for i in range(2)]
d = list(map(list,zip(*d[::-1])))

stack = []
graph = [[-1,-1] for i in range(n+1)]
par = [-1]*n
for idx,i in enumerate(d):
    x,y = i
    flag = 0
    while stack and stack[-1] > (y,idx):
        tmp = stack.pop()
        flag = 1
    if flag:
        graph[idx][0] = tmp[1]
        par[tmp[1]] = idx
    if stack:
        graph[stack[-1][1]][1] = idx
        par[idx] = stack[-1][1]
    stack.append((y,idx))

d += [[0,0]]
root = 0
for i in range(n):
    if par[i] == -1:
        root = i
        par[i] = n

w = [0]*n
def dfs(x):
    for nx in graph[x]:
        if nx != -1:
            dfs(nx)
            w[x] += w[nx]
    w[x] += d[x][0]
dfs(root)

MOD = int(1e9)+7
ans = 0
for i in range(n):
    x = w[i]*(w[i]+1)//2
    y = d[i][1]*(d[i][1]+1)//2-d[par[i]][1]*(d[par[i]][1]+1)//2
    ans = (ans+x*y)%MOD
print(ans)
    