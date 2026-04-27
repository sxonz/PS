import sys
from math import ceil
input = sys.stdin.readline

testcase = int(input())
res = []
for _ in range(testcase):
    s,h = map(int,input().split())
    hatch = []
    for i in range(h):
        x,y = map(int,input().split())
        hatch.append((x,y))

    flag = True
    for x in range(s+1):
        for y in range(s+1):
            l = 0
            if (x,y) not in hatch:
                for hx,hy in hatch:
                    l = max(l,ceil((((hx-x)**2 + (hy-y)**2)**0.5)))
                if x+l <= s and y+l <= s and x-l >= 0 and y-l >= 0:
                    res.append(str(x)+' '+str(y))
                    flag = False
                    break
        if not flag:
            break
    if flag:
        res.append('poodle')
for i in res:
    print(i)