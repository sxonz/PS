import sys
input = sys.stdin.readline
n = int(input())
sx = 0
sy = 0
sxx = 0
sxy = 0
for i in range(n):
    x,y = map(int,input().split())
    sx += x
    sy += y
    sxx += x*x
    sxy += x*y

if sx*sx == n*sxx:
    print("EZPZ")
else:
    a2 = (n*sxy - sx*sy) / (n*sxx - sx*sx)
    b2 = (sy - a2*sx) / n
    print(a2,b2)