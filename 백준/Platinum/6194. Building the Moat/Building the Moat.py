def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p3[0]-p2[0])*(p2[1]-p1[1])

def dist(p1,p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5
n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()

ans = 0
for i in range(2):
    stack = [d[0],d[1]]
    for p in d[2:]:
        while len(stack) >= 2 and ccw(stack[-2],stack[-1],p) > 0:
            stack.pop()
        stack.append(p)
    for i in range(len(stack)-1):
        ans += dist(stack[i],stack[i+1])
    d.reverse()
print("%.2f" % ans)
