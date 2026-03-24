import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

while True:
    n = int(input())
    if not n:
        break
    d = [[] for i in range(n)]
    for i in range(n-1):
        a,b,c = map(int,input().split())
        d[a].append((b,c))
        d[b].append((a,c))
    
    subtree = [0]*n
    r = [0]*n
    def sub(x,par):
        for nx,c in d[x]:
            if nx == par:
                continue
            sub(nx,x)
            subtree[x] += subtree[nx]
            r[x] += r[nx]+c*subtree[nx]
        subtree[x] += 1
    sub(0,-1)
    
    ans = int(1e12)
    def dfs(x,par,cur):
        global ans
        ans = min(ans,cur+r[x])
        tmp = sum([r[i]+c*subtree[i] for i,c in d[x] if i != par])
        for nx,c in d[x]:
            if nx == par:
                continue
            dfs(nx,x,cur+tmp+c*(n-subtree[nx])-r[nx]-c*subtree[nx])
    dfs(0,-1,0)
    print(ans)

