INF = int(1e15)

import sys
sys.setrecursionlimit(30000)
input = sys.stdin.readline

n,k = map(int,input().split())
d = [[] for i in range(n)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

mindepth = [INF]*(k+1)
centroids = [False]*n
subsize = [0]*n
curtree = []

def dfs(cur,par):
    subsize[cur] = 1
    for x,cost in d[cur]:
        if x == par or centroids[x]:
            continue
        subsize[cur] += dfs(x,cur)
    return subsize[cur]

def Centroid(cur,par,half):
    for x,cost in d[cur]:
        if x == par or centroids[x]:
            continue
        if subsize[x] > half:
            return Centroid(x,cur,half)
    return cur

def solve(cur,par,dist,depth):
    md = INF
    if dist > k:
        return INF
    for x,cost in d[cur]:
        if x == par or centroids[x]:
            continue
        md = min(md,solve(x,cur,dist+cost,depth+1))
    return min(md,mindepth[k-dist] + depth)

def update(cur,par,dist,depth):
    if dist > k:
        return
    curtree.append(dist)
    for x,cost in d[cur]:
        if x == par or centroids[x]:
           continue
        update(x,cur,dist+cost,depth+1)
    mindepth[dist] = min(mindepth[dist],depth)

res = INF
def dnc(cur):
    global curtree
    global res

    size = dfs(cur,-1)
    cent = Centroid(cur,-1,size//2)
    centroids[cent] = True
    for dist in curtree:
        mindepth[dist] = INF

    mindepth[0] = 0
    curtree = []

    for x,cost in d[cent]:
        res = min(res,solve(x,cent,cost,1))
        update(x,cent,cost,1)
    
    for x,cost in d[cent]:
        if not centroids[x]:
            dnc(x)

dnc(0)
print(res + (res == INF)*-(INF+1))