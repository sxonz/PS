import sys
input = sys.stdin.readline

MAX = 2000002
OF = 1000000
n,m = map(int,input().split())

xs = []
ys = []
xcnt = [0]*MAX
ycnt = [0]*MAX

for i in range(n):
    a,b = map(int,input().split())
    xs.append(a)
    ys.append(b)
    xcnt[a+OF] += 1
    ycnt[b+OF] += 1
    
xs.sort()
ys.sort()

xdist = [0]*MAX
ydist = [0]*MAX
xdist[0] = sum([i+OF for i in xs])
ydist[0] = sum([i+OF for i in ys])

xm,ym = 0,0
for i in range(1,MAX):
    xm += xcnt[i-1]
    ym += ycnt[i-1]
    xdist[i] = xdist[i-1]+xm+xm-n
    ydist[i] = ydist[i-1]+ym+ym-n

x,y = OF,OF
s = input().strip()
for i in s:
    if i == "S":
        y += 1
    elif i == "J":
        y -= 1
    elif i == "I":
        x += 1
    else:
        x -= 1
    print(xdist[x]+ydist[y])