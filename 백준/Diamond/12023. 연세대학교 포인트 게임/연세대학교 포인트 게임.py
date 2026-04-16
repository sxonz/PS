import sys
input = sys.stdin.readline
sys.setrecursionlimit(150001)

n = int(input())
d = [[] for i in range(n+1)]
for a in range(1,n):
    b,c = map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

subtree = [1]*(n+1)
centroids = [0]*(n+1)
r = [dict() for i in range(n+1)]
p = [-1]*(n+1)
cnt = [0]*(n+1)
s = [0]*(n+1)

def sub(par,x):
    subtree[x] = 1
    for nx,c in d[x]:
        if nx == par or centroids[nx]:
            continue
        sub(x,nx)
        subtree[x] += subtree[nx]

def centroid(par,x,size):
    for nx,c in d[x]:
        if nx == par or centroids[nx]:
            continue
        if subtree[nx] > size//2:
            return centroid(x,nx,size)
    return x

def sub2(par,x,root,l):
    r[root][x] = l
    for nx,c in d[x]:
        if nx == par or centroids[nx]:
            continue
        sub2(x,nx,root,l+c)

def dnc(cur,par):
    sub(-1,cur)
    cent = centroid(-1,cur,subtree[cur])
    centroids[cent] = 1
    p[cent] = par
    sub2(-1,cent,cent,0)
    for nx,c in d[cent]:
        if not centroids[nx]:
            dnc(nx,cent)

dnc(0,-1)
cnt = [0]*(n+1)
s = [0]*(n+1)
cnt2 = [0]*(n+1)
s2 = [0]*(n+1)

def update(x):
    node = x
    prev = -1
    while node != -1:
        cnt[node] += 1
        s[node] += r[node][x]
        if prev != -1:
            cnt2[prev] += 1
            s2[prev] += r[node][x]
        prev = node
        node = p[node]

def search(x):
    ans = 0
    node = x
    prev = -1
    while node != -1:
        ans += s[node] + cnt[node] * r[node][x]
        if prev != -1:
            ans -= s2[prev] + cnt2[prev] * r[node][x]
        prev = node
        node = p[node]
    return ans

m = int(input())
res = []
query = [0]*n
for i in range(m):
    q,x = map(int,input().split())
    if q == 1:
        if not query[x]:
            query[x]= 1
            update(x)
    else:
        res.append(search(x))
print(*res,sep='\n')