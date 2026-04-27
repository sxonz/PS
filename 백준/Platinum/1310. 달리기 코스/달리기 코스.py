import sys
input = sys.stdin.readline

n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p3[0]-p2[0])*(p2[1]-p1[1])
def area(p1,p2,p3):
    return abs(ccw(p1,p2,p3))
def distsquare(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2

d.sort()
hull = []
for h in range(2):
    stack = [d[0],d[1]]
    for i in d[2:]:
        while len(stack) >= 2 and ccw(stack[-2],stack[-1],i) <= 0:
            stack.pop()
        stack.append(i)
    hull += stack[:-1]
    d.reverse()

def distance(l,r):
    global ans
    for i in range(2):
        ans = max(ans, distsquare(hull[l],hull[(r+i)%n]))
def solve():
    l,r = 0,1
    while area(hull[-1],hull[0],hull[r]) <= area(hull[-1],hull[0],hull[(r+1)%n]):
        r += 1
    
    while l < n-1 and r < 2*n:
        if area(hull[l],hull[l+1],hull[r%n]) <= area(hull[l],hull[l+1],hull[(r+1)%n]):
            r += 1
        else:
            l += 1
        distance(l,r)
    return ans

n = len(hull)
ans = 0
if n == 2:
    print(distsquare(hull[0],hull[1]))
else:
    print(solve())