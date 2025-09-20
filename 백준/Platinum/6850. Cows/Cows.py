def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p3[0]-p2[0])*(p2[1]-p1[1])
def area(points):
    ans = 0
    n = len(points)
    for i in range(n):
        ans += points[i][0] * points[(i+1)%n][1]
        ans -= points[(i+1)%n][0] * points[i][1]
    return abs(ans) / 2

n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()

res = []
stack = [d[0],d[1]]
for i in d[2:]:
    while len(stack) >= 2 and ccw(stack[-1],stack[-2],i) <= 0:
        stack.pop()
    stack.append(i)
res += stack[:-1]

stack = [d[-1],d[-2]]
for i in list(reversed(d))[2:]:
    while len(stack) >= 2 and ccw(stack[-1],stack[-2],i) <= 0:
        stack.pop()
    stack.append(i)
res += stack[:-1]


r = area(res)
print(int(r/50))