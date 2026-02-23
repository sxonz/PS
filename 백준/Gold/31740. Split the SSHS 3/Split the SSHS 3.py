import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

v = [0]+[int(input()) for i in range(n)]
sumv = sum(v)

r = [0]*(n+1)
ans = int(1e9)
a,b = 0,0
def dfs(x,par):
    global ans,a,b
    for nx in d[x]:
        if nx == par:
            continue
        dfs(nx,x)
        tmp = abs(sumv-r[nx]-r[nx])
        if ans > tmp:
            ans = tmp
            a,b = x,nx
        r[x] += r[nx]
    r[x] += v[x]
dfs(1,-1)
print(ans)
print(a,b)