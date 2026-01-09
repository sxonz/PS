import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
color = [0]+list(map(int,input().split()))
one = color.count(1)
zero = n-one
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

c = [[0,0] for i in range(n+1)]
res = [0 for i in range(n+1)]
def dfs(x,par):
    tmp = [0,0]
    for nx in d[x]:
        if nx == par:
            continue
        dfs(nx,x)
        res[x] += c[nx][0]*tmp[1]
        res[x] += c[nx][1]*tmp[0]
        tmp[1] += c[nx][1]
        tmp[0] += c[nx][0]
        c[x][0] += c[nx][0]
        c[x][1] += c[nx][1]
    uz = zero-tmp[0]-(color[x]==0)
    uo = one-tmp[1]-(color[x]==1)
    res[x] += uz*tmp[1]
    res[x] += uo*tmp[0]
    c[x][0] += color[x]==0
    c[x][1] += color[x]==1
dfs(1,0)
for q in range(int(input())):
    print(res[int(input())])
