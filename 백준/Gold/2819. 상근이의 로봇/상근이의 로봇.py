# n = int(input())
# t = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = list(map(int,input().split()))

# dp = dict()
# dp[t[0]] = 
# for i in range(0,n):
#     pass
import sys
input = sys.stdin.readline

MAX = 2000002
OF = 1000000
n,m = map(int,input().split())

xcnt = [0]*MAX
ycnt = [0]*MAX
xdist = [0]*MAX
ydist = [0]*MAX
xdist[0] = OF*n
ydist[0] = OF*n

for i in range(n):
    a,b = map(int,input().split())
    xdist[0] += a
    ydist[0] += b
    xcnt[a+OF] += 1
    ycnt[b+OF] += 1

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