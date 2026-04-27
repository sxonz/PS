import sys
input = sys.stdin.readline

n = int(input())
l=d=100000
r=u=-100000
for i in range(n):
    x,y = map(int,input().split())
    l = min(l,x)
    r = max(r,x)
    d = min(d,y)
    u = max(u,y)
print((u-d)*(r-l))