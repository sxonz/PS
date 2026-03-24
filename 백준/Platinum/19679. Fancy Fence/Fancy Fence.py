import sys
sys.setrecursionlimit(100000)
n = int(input())
d = [tuple(map(int,input().split())) for i in range(2)]
d = list(map(list,zip(*d[::-1])))

stack = []
graph = [[-1,-1,-1] for i in range(n+1)]
for idx,i in enumerate(d):
    x,y = i
    flag = 0
    while stack and stack[-1] > (y,idx):
        tmp = stack.pop()
        flag = 1
    if flag:
        graph[idx][0] = tmp[1]
        graph[tmp[1]][2] = idx
    if stack:
        graph[stack[-1][1]][1] = idx
        graph[idx][2] = stack[-1][1]
    stack.append((y,idx))

d += [[0,0]]
root = 0
for i in range(n):
    if graph[i][2] == -1:
        root = i
        graph[i][2] = n

w = [0]*n
def dfs(x):
    for i in range(2):
        if graph[x][i] != -1:
            dfs(graph[x][i])
            w[x] += w[graph[x][i]]
    w[x] += d[x][0]
dfs(root)

MOD = int(1e9)+7
ans = 0
for i in range(n):
    x = w[i]*(w[i]+1)//2
    y = d[i][1]*(d[i][1]+1)//2-d[graph[i][2]][1]*(d[graph[i][2]][1]+1)//2
    ans = (ans+x*y)%MOD
print(ans)
    