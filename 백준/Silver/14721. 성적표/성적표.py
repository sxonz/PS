import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int,input().split())) for i in range(n)]

def f(a,x,b):
    return a*x+b

ans = int(1e9)
r = (0,0)
for a in range(1,101):
    for b in range(1,101):
        rss = 0
        for x,y in d:
            rss += (y-f(a,x,b))**2
        if rss < ans:
            ans = rss
            r = (a,b)
print(*r)
