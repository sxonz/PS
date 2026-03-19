import sys
sys.setrecursionlimit(200000)

n = int(input())
d = [int(input()) for i in range(n)]
graph = [[-1,-1] for i in range(n)]
par = [0]*n
stack = []
for idx, i in enumerate(d):
    flag = 0
    while stack and stack[-1] > (i,idx):
        tmp = stack.pop()
        flag = 1
    if stack:
        graph[stack[-1][1]][1] = idx
        par[idx] = 1
    if flag:
        graph[idx][0] = tmp[1]
        par[tmp[1]] = 1
    stack.append((i,idx))

root = par.index(0)
subtree = [0]*n
def dfs(x):
    if x == -1:
        return 0
    for nx in graph[x]:
        if nx != -1:
            subtree[x] += dfs(nx)
    subtree[x] += 1
    return subtree[x]
dfs(root)
ans = 0
for i in range(n):
    ans = max(ans,subtree[i]*d[i])
print(ans)