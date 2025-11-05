import sys
input = sys.stdin.readline
sys.setrecursionlimit(150001)

n = int(input())
nums = [0]+list(map(int,input().split()))
d = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

cent = [0]*(n+1)
subsize = [0]*(n+1)
def subtree(par,x):
    cur = 0
    for nx in d[x]:
        if cent[nx] or nx == par:
            continue
        cur += subtree(x,nx)
    subsize[x] = cur+1
    return subsize[x]

def getCentroid(r,par,x):
    for nx in d[x]:
        if nx == par or cent[nx]:
            continue
        if subsize[nx]*2 > subsize[r]:
            return getCentroid(r,x,nx)
    return x
vec = []
def collect(par,x,dist):
    global ans
    if dist > ans:
        return
    vec.append((dist,nums[x])) 
    for nx in d[x]:
        if cent[nx] or nx == par:
            continue
        collect(x,nx,dist+1)

ans = int(1e9)
mindepth = [int(1e9)]*(n+1)
used = set()
def decomp(root):
    global ans
    
    subtree(0,root)

    centroid = getCentroid(root,0,root)
    ans = min(ans,mindepth[nums[centroid]])
    mindepth[nums[centroid]] = 0
    used.add(nums[centroid])

    
    for sub in d[centroid]:
        if cent[sub]:
            continue

        vec.clear()
        
        collect(centroid,sub,1)
        for depth,val in vec:
            ans = min(ans,depth+mindepth[val])
        
        for depth,val in vec:
            if depth < mindepth[val]:
                used.add(val)
            mindepth[val] = min(mindepth[val],depth)
    for i in used:
        mindepth[i] = int(1e9)
    used.clear()
    cent[centroid] = 1
    for sub in d[centroid]:
        if cent[sub]:
            continue
        decomp(sub)
    


decomp(1)
print(ans)