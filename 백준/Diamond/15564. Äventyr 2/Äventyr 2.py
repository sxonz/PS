import sys
input = sys.stdin.readline
sys.setrecursionlimit(150001)

n,m = map(int,input().split())
d = [[] for i in range(n+1)]
tmp = list(map(int,input().split()))
for a,b in enumerate(tmp):
    d[a+2].append(b)
    d[b].append(a+2)


subtree = [1]*(n+1)
centroids = [0]*(n+1)
r = [dict() for i in range(n+1)]
p = [0]*(n+1)
cnt = [0]*(n+1)
s = [0]*(n+1)

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
    for nx in d[x]:
        if nx == par or centroids[nx]:
            continue
        sub2(x,nx,root,l+1)

def dnc(cur,par):
    sub(0,cur)
    cent = centroid(0,cur,subtree[cur])
    centroids[cent] = 1
    p[cent] = par
    sub2(0,cent,cent,0)
    for nx in d[cent]:
        if not centroids[nx]:
            dnc(nx,cent)

dnc(1,0)
s = [int(1e7)]*(n+1)

def update(x):
    node = x
    prev = 0
    while node:
        s[node] = min(r[node][x],s[node])
        node = p[node]

def search(x):
    ans = int(1e7)
    node = x
    while node:
        ans = min(ans,r[node][x]+s[node])
        node = p[node]
    return ans

res = []
query = 0
for i in range(m):
    q,x = map(int,input().split())
    if q == 1:
        query = 1
        update(x)
    else:
        if query:
            res.append(search(x))
        else:
            res.append(-1)
print(*res,sep='\n')