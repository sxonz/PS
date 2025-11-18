import sys
sys.setrecursionlimit(1000000)
n = int(input())
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    d[a].append(b)
    d[b].append(a)

def dfs(par,x):
    adp = 1
    nadp = 0
    for nx in d[x]:
        if nx != par: 
            a,b = dfs(x,nx)
            adp += min(a,b)
            nadp += a
    return (adp,nadp)

print(min(dfs(0,1)))