n = int(input())
d = list(set([tuple(map(int,input().split())) for i in range(n)]))
if len(d) == 1:
    print(0)
    exit()

def ccw(p1,p2,p3):
	return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p2[1]-p1[1])*(p3[0]-p2[0])

d.sort()
hull = []

for v in range(2):
    stack = [d[0], d[1]]
    for i in d[2:]:
        while len(stack) >= 2 and ccw(stack[-2],stack[-1],i) <= 0:
            stack.pop()
        stack.append(i)
    d.reverse()
    hull += stack[:-1]

def area(p1,p2,p3):
    return abs(ccw(p1,p2,p3))

def distsquare(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def distance(l,r):
    global ans
    for i in range(2):
        ans = max(ans,distsquare(hull[l%n],hull[(r+i)%n]))

n = len(hull)
ans = 0
for i in range(n-2):
    if ccw(hull[i],hull[i+1],hull[i+2]):
        break
else:
    print(distsquare(hull[0],hull[-1])**0.5)
    exit()

if n == 2:
    distance(0,1)
elif n >= 3:
    l,r = 0,1
    while area(hull[-1],hull[0],hull[r%n]) < area(hull[-1],hull[0],hull[(r+1)%n]):
        r += 1
        if r >= n:
            break
    while True:
        if area(hull[l%n],hull[(l+1)%n],hull[r%n]) < area(hull[l%n],hull[(l+1)%n],hull[(r+1)%n]):
            r += 1
        else:
            l += 1
        distance(l,r)
        if l>= n or r >= 2*n:
            break
print(ans**0.5)