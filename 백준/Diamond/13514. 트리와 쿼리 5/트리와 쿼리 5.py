import sys
from heapq import *
input = sys.stdin.readline
sys.setrecursionlimit(200001)

def check(x):
    for i in range(2,int(x**0.5+1)):
        if x%i == 0:
            return False
    return True

n = int(input())
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

subtree = [1]*(n+1)
centroids = [0]*(n+1)
r = [dict() for i in range(n+1)]
deleted = [dict() for i in range(n+1)]
dist = [[] for i in range(n+1)]
p = [0]*(n+1)
color = [0]*(n+1)  # 추가: 0=검정, 1=흰색

def sub(par,x):
    subtree[x] = 1
    for nx in d[x]:
        if nx == par or centroids[nx]:
            continue
        sub(x,nx)
        subtree[x] += subtree[nx]

def centroid(par,x,size):
    for nx in d[x]:
        if nx == par or centroids[nx]:
            continue
        if subtree[nx] > size//2:
            return centroid(x,nx,size)
    return x

def sub2(par,x,root,l):
    r[root][x] = l
    deleted[root][x] = 0  # 수정: 초기값 0으로 통일
    for nx in d[x]:
        if nx == par or centroids[nx]:
            continue
        sub2(x,nx,root,l+1)

def dnc(cur,par):
    sub(-1,cur)
    cent = centroid(-1,cur,subtree[cur])
    centroids[cent] = 1
    p[cent] = par
    sub2(0,cent,cent,0)
    for nx in d[cent]:
        if not centroids[nx]:
            dnc(nx,cent)

dnc(1,0)

def search(x):
    cur = int(1e7)
    node = x
    while node:
        while dist[node] and color[dist[node][0][1]] == 0:
            heappop(dist[node])
        if dist[node]:
            cur = min(cur,dist[node][0][0]+r[node][x])
        node = p[node]
    return cur if cur != int(1e7) else -1

def update(x):
    color[x] ^= 1 
    node = x
    while node:
        if color[x] == 1:
            heappush(dist[node],(r[node][x],x))
        node = p[node]

m = int(input())
ans = []
for i in range(m):
    q,x = map(int,input().split())
    if q == 1:
        update(x)
    else:
        ans.append(search(x))
print(*ans,sep='\n')