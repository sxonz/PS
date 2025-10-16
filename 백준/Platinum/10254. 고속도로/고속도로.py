import sys

input = sys.stdin.readline

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p3[0]-p2[0])*(p2[1]-p1[1])
def distsquare(p1,p2):
    return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2
def area(p1,p2,p3):
    return abs(ccw(p1,p2,p3))
def distance(l,r):
    global ans
    global p
    for i in range(2):
        tmp = distsquare(hull[l],hull[(r+i)%n])
        if tmp > ans:
            ans = tmp
            p = [l,(r+i)%n]
        


for test in range(int(input())):
    ans = 0
    p = []
    n = int(input())
    d = [tuple(map(int,input().split())) for i in range(n)]
    
    d.sort()

    hull = []
    for w in range(2):
        stack = [d[0],d[1]]
        for i in d[2:]:
            while len(stack) >= 2 and ccw(stack[-2],stack[-1],i) <= 0:
                stack.pop()
            stack.append(i)
        hull += stack[:-1]
        d.reverse()
    
    n = len(hull)
    if n == 2:
        print(*hull[0],*hull[1])
        continue
    for i in range(n-2):
        if ccw(hull[i],hull[i+1],hull[i+2]):
            break
    else:
        print(*hull[0],*hull[-1])
        continue

    l,r = 0,1
    while area(hull[-1],hull[0],hull[r]) <= area(hull[-1],hull[0],hull[(r+1)%n]):
        r = (r+1)%n

    while l < n-1 and r <= 2*n:
        if area(hull[l],hull[l+1],hull[r%n]) <= area(hull[l],hull[l+1],hull[(r+1)%n]):
            r += 1
        else:
            l += 1
        distance(l,r)
    print(*hull[p[0]],*hull[p[1]])
