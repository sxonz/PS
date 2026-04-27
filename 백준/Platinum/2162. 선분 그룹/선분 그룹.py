def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1] - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
def a(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

def line_intersection(a,b):
    fx=a[0:2]
    fy=a[2:]
    sx=b[0:2]
    sy=b[2:]
    first=ccw(fx,fy,sx)*ccw(fx,fy,sy)
    second=ccw(sx,sy,fx)*ccw(sx,sy,fy)
    if first==0 and second==0:
        if fx>fy:
            fx,fy=fy,fx
        if sx>sy:
            sx,sy=sy,sx
        if fx<=sy and sx<=fy:
            return True
        else:
            return False
    else:
        if first<=0 and second<=0:
            return True
        else:
            return False

def union(a,b):
    a_p = find(a)
    b_p = find(b)
    if b_p > a_p:
        parent[a_p] += parent[b_p]
        parent[b_p] = a_p
    else:
        parent[b_p] += parent[a_p]
        parent[a_p] = b_p

def find(x):
    if parent[x]<0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n = int(input())
parent = [-1 for _ in range(n)]
line = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if find(i) == find(j):
            continue
        else:
            if line_intersection(line[i],line[j]):
                union(i,j)
cnt = 0
max_ = 0
for i in parent:
    if i<0:
        cnt += 1
        max_ = max(-i,max_)
print(cnt)
print(max_)