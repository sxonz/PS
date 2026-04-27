def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1] - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
def a(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

tmp = ccw((x1,y1),(x2,y2),(x3,y3))
tmp2 = ccw((x1,y1),(x2,y2),(x4,y4))
tmp3 = ccw((x3,y3),(x4,y4),(x1,y1))
tmp4 = ccw((x3,y3),(x4,y4),(x2,y2))

res = 0

t = a(tmp*tmp2)
t2 = a(tmp3*tmp4)

if t == t2 == 0:
    res = 1 if max(x1,x2) >= min(x3,x4) and max(y1,y2) >= min(y3,y4) and max(x3,x4) >= min(x1,x2) and max(y3,y4) >= min(y1,y2) else 0
elif t == 0:
    res = 1 if t2 == -1 else 0
elif t2 == 0:
    res = 1 if t == -1 else 0
else:
    res = 0 if 1 in [t,t2] else 1

print(res)