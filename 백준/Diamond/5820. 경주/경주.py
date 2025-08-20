import sys
sys.setrecursionlimit(250000)
input = sys.stdin.readline

INF = int(1e15)

n,k = map(int,input().split())
d = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    d[u].append((v,w))
    d[v].append((u,w))

subsize = [0]*n
vis = [False]*n

mindepth = [INF]*(k+1)
used = []

ans = INF

def dfs(cur,par):
    subsize[cur] = 1
    for v,w in d[cur]:
        if v == par or vis[v]:
            continue
        subsize[cur]+=dfs(v,cur)
    return subsize[cur]

def centroid(cur,par,thr):
    for v,w in d[cur]:
        if v == par or vis[v]:
            continue
        if subsize[v] > thr//2:
            return centroid(v,cur,thr)
    return cur

vec = []
def collect(cur,par,dist,depth):
    global ans
    if dist>k or depth>=ans: return
    vec.append((dist,depth))
    for v,w in d[cur]:
        if v!=par and not vis[v]:
            collect(v,cur,dist+w,depth+1)

def solve(root):
    global ans
    mindepth[0] = 0
    used.append(0)

    for v,w in d[root]:
        if vis[v] or w>k: continue
        vec.clear()
        collect(v,root,w,1)

        for dist,depth in vec:
            need = k-dist
            if 0<=need<=k and mindepth[need]<INF:
                if depth+mindepth[need] < ans:
                    ans = depth+mindepth[need]

        for dist,depth in vec:
            if dist<=k and depth<mindepth[dist]:
                if mindepth[dist]==INF: used.append(dist)
                mindepth[dist] = depth

        if ans == 1:
            break

    for i in used:
        mindepth[i] = INF
    used.clear()

def dnc(cur):
    dfs(cur,-1)
    ct = centroid(cur,-1,subsize[cur])
    solve(ct)
    vis[ct] = True
    for v,w in d[ct]:
        if not vis[v]:
            dnc(v)

dnc(0)
print(-1 if ans==INF else ans)
