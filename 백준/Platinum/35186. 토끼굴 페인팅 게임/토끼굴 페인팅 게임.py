import sys
sys.setrecursionlimit(100000)

n = int(input())
d = [[] for i in range(n+1)]
parent = list(map(int,input().split()))
for i in range(n-1):
    d[parent[i]].append(i+2)

subtree = [1]*(n+1)
h = [0]*(n+1)
def sdfs(x,par):
    for nx in d[x]:
        if nx == par:
            continue
        sdfs(nx,x)
        h[x] = max(h[x],h[nx])
        subtree[x] += subtree[nx]
    h[x] += 1
sdfs(1,-1)

ans = 0
flag = True
for i in range(1,n+1):
    if subtree[i] == n//2:
        ans = max(ans,h[i])
        flag = False
if flag:
    cur = set()
    def dfs(x,par):
        global ans
        if n//2-subtree[x] in cur:
            ans = 2
        for nx in d[x]:
            if x == par:
                continue
            dfs(nx,x)
        cur.add(subtree[x])
    dfs(1,0)
            
print(ans)